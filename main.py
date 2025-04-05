from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "I am a backend and I am running."}
