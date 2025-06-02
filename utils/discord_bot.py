import os

import hikari
from dotenv import load_dotenv

load_dotenv()

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")


async def send_message_to_channel(
    coll_name: str,
    coll_amount: float,
    coll_price: float,
    debt_amount: float,
    interest_rate: float,
    txn_hash: str | None = None,
):
    rest = hikari.RESTApp()

    await rest.start()

    message = format_message(
        coll_name, coll_amount, coll_price, debt_amount, interest_rate, txn_hash
    )

    # We acquire a client with a given token. This allows one REST app instance
    # with one internal connection pool to be reused.
    async with rest.acquire(DISCORD_BOT_TOKEN, "Bot") as client:
        await client.create_message(
            CHANNEL_ID,
            embed=hikari.Embed(
                description=message,
            ),
        )

    await rest.close()


def format_message(
    coll_name: str,
    coll_amount: float,
    coll_price: float,
    debt_amount: float,
    interest_rate: float,
    txn_hash: str | None = None,
) -> str:
    coll_amount_str = (
        f"{round(coll_amount, 4):,}"
        if coll_name[-3:] == "BTC"
        else f"{round(coll_amount, 2):,}"
    )
    coll_value_str = f"(${round(coll_amount * coll_price, 2):,})"
    debt_amount_str = f"{round(debt_amount, 2):,}"
    interest_rate_str = f"{round(interest_rate, 2):,}%"
    txn_link_str = f"\n[TX](https://etherscan.io/tx/{txn_hash})" if txn_hash else ""
    emoji_str = "🔵" * min(max(int(debt_amount * 0.005), 1), 162)
    message = f"**USDaf Mint!** \n{emoji_str} \n**Collateral Deposited:** {coll_amount_str} {coll_name} {coll_value_str} \n**Minted:** {debt_amount_str} USDaf \n**Interest Rate:** {interest_rate_str} {txn_link_str}"
    return message
