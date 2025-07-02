from fastapi import FastAPI
from model import CodeInput, codereview
# from logic import get_code_review
from rag_reviewer import get_rag_review

app = FastAPI(title="LLM Code Review Bot")

# ✅ Add this root health check route
@app.get("/")
def read_root():
    return {"status": "✅ Code Review API is running"}

@app.post("/review_code", response_model=codereview)
def review_code(payload: CodeInput):
    result = get_rag_review(payload.code)
    return result