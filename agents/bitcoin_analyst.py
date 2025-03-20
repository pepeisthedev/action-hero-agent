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
    max_tokens=None,
    timeout=None,
    max_retries=2,
    http_client=httpx.Client(verify=VERIFY_SSL)
)

prompt = PromptTemplate(
    input_variables=["bitcoin_data"],
    template="""
    You are SatoshiX, the most experienced and knowledgeable Bitcoin trading AI agent. 
    Your expertise lies in analyzing Bitcoin's price movement and volatility over the past 24 hours 
    to provide actionable insights for traders.

    The given data represents the last 24 hours of Bitcoin trading activity.
    - Each entry contains **[timestamp, price, trading volume]**.

    {bitcoin_data}

    Perform a concise analysis of the past day's price movement and volatility:

    1. **Last 24-Hour Price Movement**: 
       - Summarize the overall trend (uptrend, downtrend, or sideways movement).
       - Identify the highest and lowest price points.
       - Mention any significant price swings or trends.

    2. **Volatility Insights**:
       - Measure the overall price fluctuations within the past 24 hours.
       - Analyze trading volume and its impact on price movement.
       - Comment on whether volatility is high, low, or moderate.

    Conclude with a short summary of how traders should interpret the current market conditions.
    """
)

def analyze_bitcoin_data(data):
    analyse_response = llm.invoke(prompt.format(bitcoin_data=data))
    return analyse_response
