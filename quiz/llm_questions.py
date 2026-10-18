from openai import OpenAI
from dotenv import load_dotenv
import os
import json


load_dotenv()
endpoint = os.getenv("AZURE_ENDPOINT")
model = os.getenv("AZURE_MODEL")
api_key = os.getenv("AZURE_API_KEY")


client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)


def generate_questions(topic, count):
    prompt = f"""Give me exactly {count} multiple-choice questions on {topic}.
    Reply with one JSON list only, with no extra text and no code fences. Each item in the list is one object with three keys.
    The key "question" holds the question text.
    The key "options" holds an object with exactly the keys "A", "B", "C" and "D", and each key holds the text of that choice.
    The key "answer" holds one letter, "A", "B", "C" or "D", for the correct choice.
    Spread the correct answers across all four letters."""

    try:
        response = client.responses.create(
            model=model,
            input=prompt
        )
        raw = response.output_text
        clean = raw.replace("```json", "").replace("```", "").strip()

    except Exception:
        print("Could not reach the question generator.")
        return []

    try:
        data = json.loads(clean)
    except json.JSONDecodeError:
        print("Could not load questions.")
        return []

    if not isinstance(data, list):
        return []
    else:
        return data


if __name__ == "__main__":
    result = generate_questions("Python basics", 2)
    print(result)
    print(len(result))