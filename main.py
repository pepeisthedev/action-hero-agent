from externalApis.coingecko import fetch_bitcoin_prices_24h
from externalApis.coingecko import analyze_trend
from agents.action_hero import create_action_hero_response
from twitter.twitter import post_tweet

if __name__ == "__main__":
    try:

      prices = fetch_bitcoin_prices_24h()
      trend = analyze_trend(prices)
      response = create_action_hero_response(trend, prices[-1])
      post_tweet(response.content)

    except Exception as e:
        print(f"Unexpected error: {e}")
