import os
import requests

endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
key = os.environ["AZURE_OPENAI_KEY"]
deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]

diff = open("diff.txt").read()

prompt = f"""
You are a senior software architect.

Review this code change and provide:

1. Bugs
2. Security Issues
3. Performance Risks
4. Code Quality Improvements

PR Diff:

{diff}
"""

url = f"{endpoint}/openai/deployments/{deployment}/chat/completions?api-version=2024-10-21"

headers = {
    "api-key": key,
    "Content-Type": "application/json"
}

body = {
    "messages": [
        {
            "role": "user",
            "content": prompt
        }
    ],
    "temperature": 0.2
}

response = requests.post(
    url,
    headers=headers,
    json=body
)

review = response.json()["choices"][0]["message"]["content"]

with open("review.txt", "w") as f:
    f.write(review)