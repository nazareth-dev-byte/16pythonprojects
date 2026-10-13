from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()
endpoint = os.getenv("AZURE_ENDPOINT")
model = os.getenv("AZURE_MODEL")
api_key = os.getenv("AZURE_API_KEY")


client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)

response = client.responses.create(
    model=model,
    input="what is the capital of Nigeria?",
    temperature=1.2
)

reply = response.output_text
print(f"{reply}")

"""Write one multiple-choice question about Python lists, with 4 options and the correct answer."""


