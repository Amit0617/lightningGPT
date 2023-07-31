import openai
from tenacity import retry, wait_random_exponential, stop_after_attempt
import json

openai.api_key = "sk-..." # Set your key

@retry(wait=wait_random_exponential(min=1, max=20), stop=stop_after_attempt(6))
def get_embedding(text: str, model="text-embedding-ada-002") -> list[float]:
    return openai.Embedding.create(input=[text], model=model)["data"][0]["embedding"]

text=""
file_paths=["lightning.md","cln-cheatsheet.md"]
for file_path in file_paths:
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
        embedding = get_embedding(text, model="text-embedding-ada-002")
        print(len(embedding))
    with open(file_path+"-embedding", "w", encoding="utf-8") as file:
        json.dump(embedding,file)
