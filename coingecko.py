import openai
import requests
import datetime
import os
#from dotenv import load_dotenv
import os
import certifi

#os.environ["REQUESTS_CA_BUNDLE"] = "/opt/homebrew/etc/ca-certificates/cert.pem"
#os.environ["SSL_CERT_FILE"] = "/opt/homebrew/etc/ca-certificates/cert.pem"

# Load environment variables
#load_dotenv()

# Set your API keys
COINGECKO_API_KEY = os.getenv("COINGECKO_API_KEY")

# API endpoint for CoinGecko
COINGECKO_URL = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"

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

    response = requests.get(COINGECKO_URL, headers=headers, params=params)  # Disable SSL verification
    response.raise_for_status()  # Raise error if request fails

    data = response.json()
    prices = [entry[1] for entry in data['prices']]  # Extract only the price values
    return prices

def analyze_trend(prices):
    """Analyzes price trend over the last 24 hours."""
    return "up" if prices[-1] > prices[0] else "down"