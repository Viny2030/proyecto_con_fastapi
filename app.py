from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root_message():
    return {"message": "Mi primera app con FastAPI"}