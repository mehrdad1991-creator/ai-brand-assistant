from fastapi import FastAPI

app = FastAPI(title="AI Brand Assistant")

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "AI Brand Assistant is running"}