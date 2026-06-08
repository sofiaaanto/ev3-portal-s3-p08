from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "Backend funcionando"}

@app.get("/healthz")
def health():
    return {"status": "ok"}