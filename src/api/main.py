from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Genesis v2 Life DB API — Developer Preview"}
