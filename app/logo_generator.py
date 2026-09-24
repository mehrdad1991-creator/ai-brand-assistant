# app/logo_generator.py
from app.ai_client import client

def generate_logo(brand_name: str, style: str = "minimalist, modern, vector style, white background") -> str:
    """
    Generate a logo image for a given brand name and return the image URL.
    """
    prompt = f"A professional logo for a brand named '{brand_name}'. Style: {style}."

    try:
        response = client.images.generate(
            model="gpt-image-2.5-flare",
            prompt=prompt,
            size="1024x1024",
            quality="medium",
            n=1,
        )
        # The gateway returns a URL to the generated image
        image_url = response.data[0].url
        if image_url:
            return image_url
        else:
            print("Error generating image: No URL in response")
            return None

    except Exception as e:
        print(f"Error generating image: {e}")
        return None