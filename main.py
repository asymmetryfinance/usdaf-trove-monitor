import asyncio
import os

from dotenv import load_dotenv
from rich import print
from rich.traceback import install
from web3 import AsyncWeb3, Web3, WebSocketProvider

from configs.usdaf import filters
from utils.discord_bot import send_message_to_channel
from utils.open_trove_handler import OpenTroveResult, handle_open_trove_event

install()

load_dotenv()

MAINNET_WS_RPC_URL = os.getenv("MAINNET_WS_RPC_URL")


async def main():
    async_w3 = AsyncWeb3(WebSocketProvider(MAINNET_WS_RPC_URL))

    async for w3 in async_w3:
        print(f"w3 is connected: {await w3.is_connected()}")
        print("[green]Monitoring onchain events...")
        print(f"[DEBUG] Monitoring {len(filters)} trove managers:")
        for i, f in enumerate(filters):
            print(f"[DEBUG] Filter {i+1}: {f['address'][0]}")
        
        subs_tasks = []
        # Subscribe to log filters as defined in configs files
        for f in filters:
            task = asyncio.create_task(w3.eth.subscribe("logs", f))
            subs_tasks.append(task)

        await asyncio.gather(*subs_tasks)

        async for event in w3.socket.process_subscriptions():
            open_trove_result: OpenTroveResult | None = await handle_open_trove_event(
                w3, event
            )
            if not open_trove_result:
                continue

            try:
                await send_message_to_channel(
                    coll_name=open_trove_result.coll_name,
                    coll_amount=open_trove_result.coll_amount,
                    coll_price=open_trove_result.coll_price,
                    debt_amount=open_trove_result.debt_amount,
                    interest_rate=open_trove_result.interest_rate,
                    txn_hash=open_trove_result.txn_hash,
                )
                print(f"[DEBUG] ✅ Discord message sent successfully!")
            except Exception as e:
                print(f"[DEBUG] ❌ Discord error: {e}")


if __name__ == "__main__":
    while True:
        try:
            asyncio.run(main())
        except Exception as e:
            print(e)
            continue
