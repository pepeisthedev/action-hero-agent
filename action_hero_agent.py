import openai
import requests
import datetime
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI  # Updated import
from langchain.prompts import PromptTemplate
import os
import httpx

from llmTest import httpx_client

os.environ["REQUESTS_CA_BUNDLE"] = "/opt/homebrew/etc/ca-certificates/cert.pem"
#os.environ["SSL_CERT_FILE"] = "/opt/homebrew/etc/ca-certificates/cert.pem"

# Load environment variables
load_dotenv()

# Set your API keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
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

    response = requests.get(COINGECKO_URL, headers=headers, params=params, verify=False)  # Disable SSL verification
    response.raise_for_status()  # Raise error if request fails

    data = response.json()
    prices = [entry[1] for entry in data['prices']]  # Extract only the price values
    return prices

def analyze_trend(prices):
    """Analyzes price trend over the last 24 hours."""
    return "up" if prices[-1] > prices[0] else "down"

# Setup LangChain LLM Model correctly
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=OPENAI_API_KEY,
    http_client=httpx.Client(verify=False)
)

# Define Prompt Template
prompt = PromptTemplate(
    input_variables=["price_trend", "latest_price"],
    template="""
    You are an 80s action hero. You speak in a cool, tough, and masculine way.
    Bitcoin price is currently ${latest_price:.2f} and the trend is {price_trend}.
    Respond with the latest price and the trend in your signature style with a badass quote. The quote should fit in a twitter post which is maximum 280 characters.
    """
)

if __name__ == "__main__":
    try:
        # Fetch Bitcoin prices for the last 24 hours
        prices = fetch_bitcoin_prices_24h()
        print("Fetched prices")
        trend = analyze_trend(prices)
        latest_price = prices[-1]
        print(f"Latest price: {latest_price}")

        # Use LangChain to generate response
        hero_response = llm.invoke(prompt.format(price_trend=trend, latest_price=latest_price))

        print(hero_response)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Bitcoin data: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
