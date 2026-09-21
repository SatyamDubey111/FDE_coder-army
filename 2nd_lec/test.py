from fastapi import FastAPI

app = FastAPI(title="FDE Course API")


@app.get("/")
def home():
    return {
        "message": "FDE FastAPI is working!"
    }


@app.get("/hello")
def hello():
    return {
        "message": "Hello from FastAPI"
    }