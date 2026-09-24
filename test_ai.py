from app.ai_client import client, MODEL_NAME

response = client.chat.completions.create(
    model=MODEL_NAME,
    messages=[
        {"role": "user", "content": "Say 'Hello from AI Brand Assistant!' in one short sentence."}
    ]
)

print("AI Response:")
print(response.choices[0].message.content)