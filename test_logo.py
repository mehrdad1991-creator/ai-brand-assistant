from app.ai_client import client
import json

print("Testing image generation...")

try:
    response = client.images.generate(
        model="gpt-image-2.5-flare",
        prompt="A minimalist logo for a coffee shop called Bean & Being",
        size="1024x1024",
        quality="medium",
        n=1,
    )
    print("=== FULL RESPONSE ===")
    print(response)
    print("\n=== RESPONSE DATA ===")
    print(response.data)
    print("\n=== FIRST ITEM ===")
    print(response.data[0])
    print("\n=== FIRST ITEM FIELDS ===")
    print(dir(response.data[0]))
    print("\n=== AS DICT (if possible) ===")
    try:
        print(response.data[0].model_dump())
    except Exception as e:
        print("Could not dump:", e)

except Exception as e:
    print("FAILED!")
    print("Error type:", type(e).__name__)
    print("Error message:", str(e))