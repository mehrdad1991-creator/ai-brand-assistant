from app.brand_kit import generate_brand_kit

business_description = "A cozy, organic coffee shop in Tehran targeting young professionals who love specialty coffee and a calm atmosphere."

print("Generating brand kit...\n")

brand_kit = generate_brand_kit(business_description)

print("=== BRAND NAMES ===")
for name in brand_kit["brand_names"]:
    print(f"  - {name}")

print("\n=== TAGLINES ===")
for tagline in brand_kit["taglines"]:
    print(f"  - {tagline}")

print("\n=== SOCIAL POST ===")
print(f"  {brand_kit['social_post']}")

print("\n=== COLOR PALETTE ===")
for color in brand_kit["color_palette"]:
    print(f"  {color['name']}: {color['hex']}")

print("\n=== FONT PAIRING ===")
print(f"  Heading: {brand_kit['font_pairing']['heading']}")
print(f"  Body: {brand_kit['font_pairing']['body']}")

print("\n=== TARGET AUDIENCE ===")
print(f"  {brand_kit['target_audience']}")