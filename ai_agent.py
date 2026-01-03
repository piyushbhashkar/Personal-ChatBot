
# Phase1- Create AI Agent

# TAVILY_API_KEY was not picked up from .env file , so trying a diff way
from dotenv import load_dotenv
load_dotenv()  # reads .env in current working directory

# 1.> Set up API keys for Groq and Tavily ( To power LLMs with lastest information)
import os

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")

# 2.> Setup LLM and Tools

from  langchain_groq import ChatGroq
from  langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults


openai_llm = ChatOpenAI(model="gpt-4o-mini")
groq_llm = ChatGroq(model="llama-3.3-70b-versatile")
search_tool=TavilySearchResults(max_results=2)

# 3.> Set AI Agent with Search tool functionality 
from langgraph.prebuilt import create_react_agent

system_prompt = "Act as a ChatBot who is smart and friendly"

agent = create_react_agent(
    model = groq_llm,
    tools = [search_tool],
    prompt = system_prompt # state_modifier = system_prompt has become obsoleate 
)

query ="Tell me about the trends in crypto"
state ={"messages": query}
response =agent.invoke(state)
print(response)







