from langchain_openai import AzureChatOpenAI
import openai
import os
from dotenv import load_dotenv, find_dotenv
from openai import AzureOpenAI

# Load environment variables from the .env file
load_dotenv(find_dotenv())

endpoint = os.getenv("AZURE_OPENAI_API_BASE")
key = os.getenv("AZURE_OPENAI_API_KEY")  # Your API key 
model_name = "gpt-4o-mini"  # Your model name

# client = AzureOpenAI(azure_endpoint=endpoint,api_version="2024-02-01",api_key=key)
# completion = client.chat.completions.create(
# model=model_name,
# messages=[{"role": "user",
#     "content": "What is AI?",  # Your question can go here
#   },], 
# )
# print(completion.choices[0].message.content)


llm = AzureChatOpenAI(
    deployment_name=model_name,
    api_key=key,
    azure_endpoint=endpoint,
    api_version="2024-02-01",
)
messages = [
    (
        "system",
        "You are a helpful translator. Translate the user sentence to French.",
    ),
    ("human", "I love programming."),
]
print(llm.invoke(messages))

