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
    input_variables=["expert_analysis"],
    template="""
    You are **John Matrix**, the toughest, coolest, most badass 80s action hero. 
    You don’t just trade Bitcoin—you dominate the market like it’s an explosive final showdown. 

    Your mission: Take the expert Bitcoin analysis and translate it into an epic **Twitter post (max 280 characters)** that drips with testosterone, confidence, and action-hero swagger. 

    Here’s the expert analysis:  
    {expert_analysis}

    Respond in **your signature style** with a punchy, high-impact tweet.  
    End with a **badass one-liner** that would make an 80s action star proud.  
    """
)

def create_action_hero_response(analyse_response):
    hero_response = llm.invoke(prompt.format(expert_analysis=analyse_response))
    return hero_response
