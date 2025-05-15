from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Now you can access the environment variables
langchain_api_key = os.getenv('LANGCHAIN_API_KEY')
tracing = os.getenv('LANGCHAIN_TRACING_V2')
openai_api_key = os.getenv('OPENAI_API_KEY')
tavily_api_key = os.getenv('TAVILY_API_KEY')

# Print the variables to check if they are correctly loaded
if langchain_api_key:
    print(f"LANGCHAIN_API_KEY: {langchain_api_key}")
else:
    print("LANGCHAIN_API_KEY is not set!")

if tracing:
    print(f"LANGCHAIN_TRACING_V2: {tracing}")
else:
    print("LANGCHAIN_TRACING_V2 is not set!")

if openai_api_key:
    print(f"OPENAI_API_KEY: {openai_api_key}")
else:
    print("OPENAI_API_KEY is not set!")

if tavily_api_key:
    print(f"TAVILY_API_KEY: {tavily_api_key}")
else:
    print("TAVILY_API_KEY is not set!")
