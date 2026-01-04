# Phase 3 - Setup FrontEnd

# 1.> Setup UI with stremlit ( model provider , model , system prompt , query )
# import streamlit as st

# st.set_page_config(page_title="Langgraph AI Agent", layout="Wide")
# st.title("AI ChatBot Agent")
# st.write("Create and Interact with AI agnet!")


import streamlit as st
import requests

API_URL = "http://127.0.0.1:9999/chat"  # your FastAPI endpoint

st.set_page_config(page_title="LangGraph AI Agent", layout="wide")
st.title("AI ChatBot Agent")
st.write("Create and interact with your LangGraph + FastAPI agent.")

# Sidebar: model provider & model
with st.sidebar:
    st.header("Model Settings")
    provider = st.selectbox("Model provider", ["Groq", "OpenAI"])

    if provider == "Groq":
        model_name = st.selectbox(
            "Model",
            ["llama-3.1-8b-instant", "mixtral-8x7b-32768", "llama-3.3-70b-versatile"],
        )
    else:
        model_name = st.selectbox("Model", ["gpt-4o-mini"])

    allow_search = st.checkbox("Enable web search (Tavily)", value=True)

system_prompt = st.text_area(
    "System prompt",
    value="Act as a ChatBot who is smart and friendly",
    height=80,
)

user_query = st.text_area("Your message", height=120)

if st.button("Send"):
    if not user_query.strip():
        st.warning("Please enter a message first.")
    else:
        payload = {
            "model_name": model_name,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_search,
        }

        try:
            resp = requests.post(API_URL, json=payload, timeout=60)
            if resp.status_code == 200:
                data = resp.json()
                # if your backend returns plain string, data is the answer
                # if it returns {"answer": "..."} adjust accordingly
                st.subheader("Assistant:")
                st.write(data if isinstance(data, str) else data.get("answer", data))
            else:
                st.error(f"API error {resp.status_code}: {resp.text}")
        except Exception as e:
            st.error(f"Request failed: {e}")







# 2. Connect with backend via URL