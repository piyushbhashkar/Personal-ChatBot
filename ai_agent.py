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
# Adding on as backend.py is unable to import ai_agent.py class get_response_from_ai_agent
from langchain_tavily import TavilySearch  
from langchain_core.messages import HumanMessage, AIMessage

openai_llm = ChatOpenAI(model="gpt-4o-mini")
groq_llm = ChatGroq(model="llama-3.3-70b-versatile")
search_tool=TavilySearchResults(max_results=2)

# 3.> Set AI Agent with Search tool functionality 
from langgraph.prebuilt import create_react_agent
# Updating below after initail success till line print(response)
from langchain_core.messages.ai import AIMessage


system_prompt = "Act as a ChatBot who is smart and friendly"


# def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
#     if provider=="Groq":
#         llm=ChatGroq(model=llm_id)
#     elif provider=="OpenAI":
#         llm=ChatOpenAI(model=llm_id)

#     tools=[TavilySearchResults(max_results=2)] if allow_search else []
#     agent=create_react_agent(
#         model=llm,
#         tools=tools,
#         prompt=system_prompt
#     )
#     state={"messages": query}
#     response=agent.invoke(state)
#     messages=response.get("messages")
#     ai_messages=[message.content for message in messages if isinstance(message, AIMessage)]
#     return ai_messages[-1]


def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    if provider == "Groq":
        llm = ChatGroq(model=llm_id)
    elif provider == "OpenAI":
        llm = ChatOpenAI(model=llm_id)
    else:
        raise ValueError(f"Unsupported provider: {provider}")

    tools = [TavilySearchResults(max_results=2)] if allow_search else []


    agent = create_react_agent(
        model=llm,
        tools=tools,
        prompt=system_prompt,            
    )

    if isinstance(query, str):
        messages_in = [HumanMessage(content=query)]
    else:
        messages_in = [HumanMessage(content=m) for m in query]

    state = {"messages": messages_in}

    response = agent.invoke(state)
    messages = response.get("messages", [])

    ai_messages = [message for message in messages if isinstance(message, AIMessage)]
    return ai_messages[-1].content if ai_messages else ""











