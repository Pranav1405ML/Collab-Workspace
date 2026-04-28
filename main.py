from fastapi import FastAPI
from pydantic import BaseModel

class CodePayload(BaseModel):
    code: str

app = FastAPI()

# In-memory storage
storage = {"code": ""}

@app.get("/status")
def status():
    return {"state":"alive"}

# GET /code — returns whatever is currently stored
@app.get("/code")
def get_code():
    return storage["code"]

# POST /code — receives code and stores it
@app.post("/code")
def save_code(payload: CodePayload):
    storage["code"] = payload.code
    return "Code stored successfully"