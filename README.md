# USDaf Trove Monitor

## Requirements

This project is managed using `uv`

```bash
pip install uv
```

or

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

You will also need:

- A Discord bot token
- A Discord channel ID for the bot to send messages to
- Websocket RPC URL for Ethereum Mainnet

## Setup

```bash
git clone https://github.com/pastelfork/usdaf-trove-monitor
```

```bash
cd usdaf-trove-monitor
```

```bash
cp .env.example .env
```

Paste your enviroment variables in the .env file (see requirements above).

```bash
uv run main.py
```

The bot should now be running and monitoring blockchain logs in realtime.
