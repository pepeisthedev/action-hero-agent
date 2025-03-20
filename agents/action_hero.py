import openai
import requests
from langchain_openai import ChatOpenAI  # Updated import
from langchain.prompts import PromptTemplate
import httpx
from config import VERIFY_SSL

# Setup LangChain LLM Model correctly
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=1.2,
    model_kwargs={"top_p": 0.9},
    max_tokens=None,
    timeout=None,
    max_retries=2,
    http_client=httpx.Client(verify=VERIFY_SSL)
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

def create_action_hero_response(trend, latest_price):
    hero_response = llm.invoke(prompt.format(price_trend=trend, latest_price=latest_price))
    return hero_response
