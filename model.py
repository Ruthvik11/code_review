from pydantic import BaseModel

class CodeInput(BaseModel):
    code:str



class codereview(BaseModel):
    review: str
    sources: list[str]