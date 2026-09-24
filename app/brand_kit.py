import json
from app.ai_client import client, MODEL_NAME


def generate_brand_kit(business_description: str) -> dict:
    """
    Generate a complete brand kit from a business description.
    Returns a dictionary with names, taglines, social copy, colors, and fonts.
    """

    system_prompt = """You are a professional brand strategist and copywriter.
You will receive a description of a business and must generate a complete brand starter kit.
You MUST return ONLY valid JSON, with no additional text or explanations.
The JSON must follow this exact structure:
{
  "brand_names": ["name1", "name2", "name3"],
  "taglines": ["tagline1", "tagline2", "tagline3"],
  "social_post": "A short, engaging social media post (2-3 sentences).",
  "color_palette": [
    {"name": "Primary", "hex": "#XXXXXX"},
    {"name": "Secondary", "hex": "#XXXXXX"},
    {"name": "Accent", "hex": "#XXXXXX"},
    {"name": "Background", "hex": "#XXXXXX"},
    {"name": "Text", "hex": "#XXXXXX"}
  ],
  "font_pairing": {
    "heading": "Font name for headings",
    "body": "Font name for body text"
  },
  "target_audience": "A short description of who this brand is for."
}
"""

    user_prompt = f"Business description: {business_description}"

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        response_format={"type": "json_object"},
        temperature=0.8,
    )

    raw_content = response.choices[0].message.content

    try:
        brand_kit = json.loads(raw_content)
    except json.JSONDecodeError as e:
        raise ValueError(f"AI returned invalid JSON: {e}\nRaw content: {raw_content}")

    return brand_kit