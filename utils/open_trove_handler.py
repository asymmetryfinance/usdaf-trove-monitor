from dataclasses import dataclass

from eth_abi import decode
from web3 import Web3

from configs import usdaf

PRECISION = 10**18


@dataclass
class OpenTroveResult:
    coll_name: str
    coll_amount: float
    coll_price: float
    debt_amount: float
    interest_rate: float
    txn_hash: str


async def handle_open_trove_event(w3, event: dict):
    # also handles adjust trove events
    topic0 = Web3.to_hex(event["result"]["topics"][0])
    if topic0 != usdaf.topic0:  # not a TroveOperation event
        return None

    (
        _operation,
        _annualInterestRate,
        _debtIncreaseFromRedist,
        _debtIncreaseFromUpfrontFee,
        _debtChangeFromOperation,
        _collIncreaseFromRedist,
        _collChangeFromOperation,
    ) = decode(
        ["uint8", "uint256", "uint256", "uint256", "int256", "uint256", "int256"],
        event["result"]["data"],
    )

    if (
        _operation != 0 and _operation != 2 and _operation != 7
    ):  # not an openTrove/adjustTrove/openTroveAndJoinBatch operation - see ITroveEvents.sol
        return None

    if _debtChangeFromOperation < 0:
        # no USDaf minted
        return None

    # we only track collateral deposited
    _collChangeFromOperation = (
        0 if _collChangeFromOperation < 0 else _collChangeFromOperation
    )

    # find the branch from config which this event corresponds to
    branch = next(
        (
            (k, v)
            for k, v in usdaf.branches.items()
            if v["trove_manager"]
            == Web3.to_checksum_address(event["result"]["address"])
        ),
        None,
    )
    if branch:
        coll_name, branch_config = branch

    # get the price of the collateral from the price feed
    price_feed = w3.eth.contract(
        address=branch_config["price_feed"],
        abi="""[{"inputs":[],"name":"lastGoodPrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]""",
    )
    coll_price: float = await price_feed.functions.lastGoodPrice().call() / PRECISION

    return OpenTroveResult(
        coll_name=coll_name,
        coll_amount=_collChangeFromOperation / PRECISION,
        coll_price=coll_price,
        debt_amount=_debtChangeFromOperation / PRECISION,
        interest_rate=_annualInterestRate / 10**16,  # convert to percentage
        txn_hash=Web3.to_hex(event["result"]["transactionHash"]),
    )
