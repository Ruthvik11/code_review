from model import CodeInput
from prompt import get_prompt_review
#from model_loader import run_model
import openai
from dotenv import load_dotenv
import os
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_code_review(code:str)->str:
    prompt = get_prompt_review(code)

    response = openai.chat.completions.create(
       model = "gpt-3.5-turbo",
       messages =[
           {"role":"system","content":"you are a python code ai assistant who debugs the code provided by the user ."},
           {"role":"user","content":prompt}
       ],
       temperature = 0.7,
       max_tokens = 500
    )

    return response.choices[0].message.content
