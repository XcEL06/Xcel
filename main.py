from fastapi import FastAPI

app = FastAPI(title="Ad Platform API", version="1.0")

@app.get("/")
def home():
    return {"message": "Welcome to the Global Ad Platform API!"
