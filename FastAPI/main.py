from fastapi import FastAPI

app = FastAPI()

@app.post("/analyze-text")
def analyze_text(text: str):
    if "bleeding" in text:
        return {"injury": "bleeding", "severity": "high"}
    return {"injury": "unknown", "severity": "low"}