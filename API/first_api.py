from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Привет!"}

@app.get("/llo/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}!!"}