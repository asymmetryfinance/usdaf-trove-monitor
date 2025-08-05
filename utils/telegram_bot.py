import os

from dotenv import load_dotenv
from rich import print
from rich.traceback import install
from telegram import Bot

install()

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


async def send_message_to_tg(
    coll_name: str,
    coll_amount: float,
    coll_price: float,
    debt_amount: float,
    interest_rate: float,
    txn_hash: str | None = None,
):
    bot = Bot(TELEGRAM_BOT_TOKEN)
    message = format_message(
        coll_name, coll_amount, coll_price, debt_amount, interest_rate, txn_hash
    )
    async with bot:
        # print(await bot.get_me())
        # updates = await bot.get_updates()
        # print(updates)
        await bot.send_message(text=message, chat_id=TELEGRAM_CHAT_ID)


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
    coll_value_str = (
        f"(${round(coll_amount * coll_price, 2):,})" if coll_amount > 0 else ""
    )
    debt_amount_str = f"{round(debt_amount, 2):,}"
    interest_rate_str = f"{round(interest_rate, 2):,}%"
    txn_link_str = f"\nTX: https://etherscan.io/tx/{txn_hash}" if txn_hash else ""
    emoji_str = ""
    message = f"USDaf Mint! \n{emoji_str} \nCollateral Deposited: {coll_amount_str} {coll_name} {coll_value_str} \nMinted: {debt_amount_str} USDaf \nInterest Rate: {interest_rate_str} {txn_link_str}"
    return message