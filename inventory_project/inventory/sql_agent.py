# import os
# from langchain_community.utilities import SQLDatabase
# from langchain_groq import ChatGroq
# from sqlalchemy.exc import SQLAlchemyError
# from urllib.parse import quote_plus
# from langchain.utilities import SQLDatabase
# # from langchain.llms import OpenAI
# from langchain.agents import create_sql_agent
# from langchain.agents.agent_toolkits import SQLDatabaseToolkit
# from langchain.agents.agent_types import AgentType
# # Database connection (fixing the incorrect password format)

# GROQ_API_KEY = "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"
# if not GROQ_API_KEY:
#     raise ValueError("Groq API Key is missing! Set GROQ_API_KEY in environment variables.")
# username = "postgres"
# password = quote_plus("Chetu@123")  # URL-encode special characters
# host = "localhost"
# database = "SqlAgentInventory"

# DATABASE_URL = f"postgresql+psycopg2://{username}:{password}@{host}/{database}"

# try:
#     db = SQLDatabase.from_uri(DATABASE_URL)
#     db.get_usable_table_names()
# except SQLAlchemyError as e:
#     raise Exception(f"Database connection failed: {e}")

# # Use Groq's Llama 3 model
# llm = ChatGroq(
#     model="llama-3.3-70b-versatile",
#     temperature=0,
#     verbose=True,
#     api_key=GROQ_API_KEY,
# )


# agent_executor = create_sql_agent(
#     llm=llm,
#     toolkit=SQLDatabaseToolkit(db=db, llm=llm),
#     verbose=True,
#     agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
# )


# # agent_executor.run(
# #     "How many products are there?"
# # )

# def process_query(query):
#     """Process the user query and return response."""
#     try:
#         response = agent_executor.run(query)
#         return response
#     except Exception as e:
#         return str(e)




import os
from langchain_community.utilities import SQLDatabase
from langchain_groq import ChatGroq
from sqlalchemy.exc import SQLAlchemyError
from urllib.parse import quote_plus
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType

# Database connection
GROQ_API_KEY = "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"
if not GROQ_API_KEY:
    raise ValueError("Groq API Key is missing! Set GROQ_API_KEY in environment variables.")

username = "postgres"
password = quote_plus("Chetu@123")  # URL-encode special characters
host = "localhost"
database = "SqlAgentInventory"

DATABASE_URL = f"postgresql+psycopg2://{username}:{password}@{host}/{database}"

try:
    db = SQLDatabase.from_uri(DATABASE_URL)
    db.get_usable_table_names()
except SQLAlchemyError as e:
    raise Exception(f"Database connection failed: {e}")

# Use Groq's Llama 3 model
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    verbose=True,
    api_key=GROQ_API_KEY,
)

agent_executor = create_sql_agent(
    llm=llm,
    toolkit=SQLDatabaseToolkit(db=db, llm=llm),
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)

def process_query(query):
    """Process the user query and return response."""
    try:
        response = agent_executor.run(query)
        return response
    except Exception as e:
        return str(e)
