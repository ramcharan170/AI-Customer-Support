from agents.llm import client, MODEL_NAME

response = client.chat.completions.create(
    model=MODEL_NAME,
    messages=[
        {
            "role": "user",
            "content": "Reply with only the word: SUCCESS"
        }
    ],
    temperature=0,
)

print(response.choices[0].message.content)