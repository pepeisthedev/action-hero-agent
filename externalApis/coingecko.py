import openai
import requests
import os
from config import VERIFY_SSL
from datetime import datetime

# Set your API keys
COINGECKO_API_KEY = os.getenv("COINGECKO_API_KEY")

# API endpoint for CoinGecko
COINGECKO_URL = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"

def extract_hourly_data(api_response):
    prices = api_response["prices"]
    volumes = api_response["total_volumes"]

    hourly_data = []
    seen_hours = set()  # Track already processed hours

    for i in range(len(prices)):
        timestamp, price = prices[i]
        _, volume = volumes[i]

        # Convert timestamp to "YYYY-MM-DD HH:00" (hourly format)
        hour = datetime.utcfromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:00')

        # Only store the first occurrence for each hour
        if hour not in seen_hours:
            hourly_data.append([timestamp, price, volume])
            seen_hours.add(hour)

    return hourly_data

def fetch_bitcoin_prices_24h():
    """Fetches Bitcoin prices over the last 24 hours from CoinGecko."""
    params = {
        "days": 1,
        "vs_currency": "usd"
    }
    headers = {
        "accept": "application/json",
        "x-cg-api-key": COINGECKO_API_KEY
    }

    response = requests.get(COINGECKO_URL, headers=headers, params=params, verify=VERIFY_SSL)
    response.raise_for_status()  # Raise error if request fails

    return extract_hourly_data(response.json())
