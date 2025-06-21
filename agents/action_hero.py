import openai
import requests
from langchain_openai import AzureChatOpenAI  # Updated import
from langchain.prompts import PromptTemplate
import httpx
from config import VERIFY_SSL

# Setup LangChain LLM Model correctly
llm = AzureChatOpenAI(
    model="gpt-4o-mini",
    temperature=1.2,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    http_client=httpx.Client(verify=VERIFY_SSL)
)

prompt = PromptTemplate(
    input_variables=["expert_analysis"],
    template="""
    You are **John Matrix**, the toughest, coolest, most badass 80s action hero. 
    You don’t just trade Bitcoin—you dominate the market like it’s an explosive final showdown. 

    Your mission: Take the expert Bitcoin analysis and translate it into an epic **Twitter post (strictly max 280 characters, no hashtags)** that drips with testosterone, confidence, and action-hero swagger. 

    - Make it **short, punchy, and impactful**.
    - Do **not** exceed **280 characters**. If necessary, **cut unnecessary words** while keeping the attitude.
    - End with a **badass one-liner** worthy of an 80s action star.

    Here’s the expert analysis:  
    {expert_analysis}

    Respond with a **single tweet** that follows all the above rules.
    """
)


def create_action_hero_response(analyse_response):
    hero_response = llm.invoke(prompt.format(expert_analysis=analyse_response))
    content = hero_response.content
    if len(content) > 280:
        print(f"Warning: Response exceeded 280 characters ({len(content)}). Truncating.")
        content = content[:277] + "..."
        # Create a new response object with truncated content
        hero_response.content = content
    return hero_response
