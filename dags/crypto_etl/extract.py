import os
import requests
from datetime import datetime, timezone

COINS = ["bitcoin","ethereum","solana"]

BASE_URL = "https://api.coingecko.com/api/v3/coins/markets"

def extract(coins=COINS):
    api_key = os.environ.get("COINGECKO_API_KEY")

    if not api_key:
        raise ValueError("COINGECKO_API_KEY IS NOT SET")

    params = {
        "vs_currency": "usd",
        "ids": ",".join(COINS),
        "orders": "market_cap_desc",
        "per_page": len(COINS),
        "page": 1,
        "sparkline": "false"

    }

    headers = {
        "x-cg-demo-api-key": api_key
    }

    response = requests.get(
        BASE_URL,
        headers=headers,
        params=params,
        timeout=30
    )

    response.raise_for_status()
    return response.json()