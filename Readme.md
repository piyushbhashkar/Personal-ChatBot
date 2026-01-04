# To install pipenv
pip uninstall pipenv
pip install pipenv
pipenv --version
# To load environment variable 
pipenv shell
# To install different langchain libraries 
pipenv install langchain_groq langchain_openai langchain_community
# To install agents
pipenv install langgraph
# To install latest tavily
<!-- pipenv install "langchain-community[tavily]"
pipenv install tavily-python -->
pip install -U langchain-tavily tavily-python
# TAVILY_API_KEY was not picked up from .env file , so trying a diff way
pipenv install python-dotenv


# Start of 2nd phase , backend.py 
pipenv install pydantic
pipenv install fastapi

# To set up UI
pipenv install uvicorn 

# To run the frontend 
streamlit run frontend.py






