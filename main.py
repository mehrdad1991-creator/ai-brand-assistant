from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from app.brand_kit import generate_brand_kit
from app.logo_generator import generate_logo

app = FastAPI(title="AI Brand Assistant")

app.mount("/static", StaticFiles(directory="static"), name="static")

class BrandRequest(BaseModel):
    business_description: str

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "AI Brand Assistant is running"}

@app.get("/")
def serve_frontend():
    return FileResponse("static/index.html")

@app.post("/api/generate")
def generate_brand(request: BrandRequest):
    if not request.business_description.strip():
        raise HTTPException(status_code=400, detail="Business description cannot be empty")
    
    try:
        # 1. Generate the text-based brand kit
        brand_kit = generate_brand_kit(request.business_description)
        
        # 2. Generate a logo image using the first suggested brand name
        if brand_kit and brand_kit.get("brand_names"):
            first_brand_name = brand_kit["brand_names"][0]
            logo_url = generate_logo(first_brand_name)
            brand_kit["logo_url"] = logo_url # Add the logo URL to the response
        else:
            brand_kit["logo_url"] = None

        return brand_kit
    except Exception as e:
        # Log the error for debugging
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="An internal error occurred while generating the brand kit.")