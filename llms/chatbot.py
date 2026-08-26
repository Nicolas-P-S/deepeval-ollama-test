import ollama
import json
from pathlib import Path

dir = Path(__file__).resolve().parent.parent
model = "qwen2.5:7b"

with open(dir/"data"/"catalogo.json", "r", encoding="utf-8") as file:
    catalogo = json.load(file)

with open(dir/"data"/"prompt_ruim.txt", "r", encoding="utf-8") as file:
    prompt = file.read()

def perguntar_chat(input: str, model = model):
    sys_message= f"""
    {prompt}

    Catálogo:
    {json.dumps(catalogo, ensure_ascii=False, indent=2)}
    """
    res = ollama.chat(model=model, messages=[
        {"role": "system", "content": sys_message},
        {"role": "user", "content": input}
    ])

    return res["message"]["content"]
