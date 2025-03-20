import os
import json
import traceback
from requests_oauthlib import OAuth1Session
from config import VERIFY_SSL

def post_tweet(tweet_text):
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("TWITTER_ACCESS_TOKEN")  # Pre-saved token
    access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")  # Pre-saved secret

    if not all([consumer_key, consumer_secret, access_token, access_token_secret]):
        raise ValueError("Missing Twitter API credentials in environment variables.")

    try:
        # Prepare tweet payload
        payload = {"text": tweet_text}

        # Authenticate using the saved access token
        oauth = OAuth1Session(
            consumer_key,
            client_secret=consumer_secret,
            resource_owner_key=access_token,
            resource_owner_secret=access_token_secret,
        )

        # Send tweet
        response = oauth.post("https://api.twitter.com/2/tweets", json=payload, verify=VERIFY_SSL)

        if response.status_code != 201:
            raise Exception(f"Error {response.status_code}: {response.text}")

        print("Tweet posted successfully!")
        print(json.dumps(response.json(), indent=4, sort_keys=True))

    except Exception as e:
        print("Error Type:", type(e).__name__)  # Type of error
        print("Error Message:", e)  # Error message
        print("Traceback Details:")
        traceback.print_exc()  # Print full traceback

