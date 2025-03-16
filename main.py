from coingecko import fetch_bitcoin_prices_24h
from coingecko import analyze_trend
from action_hero_agent import create_action_hero_response

if __name__ == "__main__":
    try:
        # Fetch Bitcoin prices for the last 24 hours
        prices = fetch_bitcoin_prices_24h()
        trend = analyze_trend(prices)
        response = create_action_hero_response(trend, prices[-1])
        print(response.content)

    except Exception as e:
        print(f"Unexpected error: {e}")
