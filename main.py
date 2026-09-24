from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from app.brand_kit import generate_brand_kit

app = FastAPI(title="AI Brand Assistant")

# Mount static files (HTML, CSS, JS)
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
        brand_kit = generate_brand_kit(request.business_description)
        return brand_kit
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))