"""from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

model_id = "deepseek-ai/deepseek-coder-6.7b-instruct"

tokenizer = AutoTokenizer.from_pretrained(model_id)

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",
    torch_dtype="auto",
    offload_folder="./offload"  # this tells it where to store offloaded weights
)

def run_model():
    codepipe = pipeline("text-generation", model=model, tokenizer=tokenizer)
    return codepipe"""