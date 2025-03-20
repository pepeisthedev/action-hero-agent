from externalApis.coingecko import fetch_bitcoin_prices_24h
from agents.action_hero import create_action_hero_response
from agents.bitcoin_analyst import analyze_bitcoin_data
from twitter.twitter import post_tweet

if __name__ == "__main__":
    try:

      prices = fetch_bitcoin_prices_24h()
      analyse_response = analyze_bitcoin_data(prices)
    #  print(response)
      response = create_action_hero_response(analyse_response.content)
      post_tweet(response.content)

    except Exception as e:
        print(f"Unexpected error: {e}")
