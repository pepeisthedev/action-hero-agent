import os

# Determine if running locally or on Railway
RUNNING_LOCALLY = 'RAILWAY_ENVIRONMENT' not in os.environ

# Set verify flag based on environment
VERIFY_SSL = not RUNNING_LOCALLY

# Load environment variables if running locally
if RUNNING_LOCALLY:
    try:
        from dotenv import load_dotenv
        load_dotenv()
        print("Loaded environment variables from .env file")
    except ImportError:
        print("python-dotenv not installed, skipping .env loading")