from fastapi import FastAPI
from pydantic import BaseModel
from database import SessionLocal, CodeSnippet

class CodePayload(BaseModel):
    code: str

app = FastAPI()

# GET /code — returns whatever is currently stored
@app.get("/code")
def get_code():
    session = SessionLocal()
    snippet = session.query(CodeSnippet).order_by(CodeSnippet.id.desc()).first()
    session.close()
    return {"code" : snippet.code}

# POST /code — receives code and stores it
@app.post("/code")
def save_code(payload: CodePayload):
    session = SessionLocal()
    snippet = CodeSnippet(code=payload.code)
    session.add(snippet)
    session.commit()
    session.close()
    return "Code Saved"
