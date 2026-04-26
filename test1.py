# app.py
# Ví dụ API cực đơn giản dùng FastAPI + Ollama
# Khi gọi /ask sẽ trả lời "hello" từ model
# uvicorn test1:app --reload

from fastapi import FastAPI
import string
import requests

app = FastAPI()

OLLAMA_URL = "http://localhost:11434/api/generate"

@app.get("/")
def home():
    return {"message": "API is running"}


def build_prompt(messages, system=None, think=False):
    prompt = ""

    # system
    if system:
        prompt += "<|im_start|>system\n"
        prompt += system + "\n"
        prompt += "<|im_end|>\n"

    # messages
    for i, msg in enumerate(messages):
        role = msg["role"]
        content = msg["content"]

        prompt += f"<|im_start|>{role}\n"
        prompt += content

        # nếu là user cuối
        if role == "user" and i == len(messages) - 1:
            prompt += " /think" if think else " /no_think"

        prompt += "\n<|im_end|>\n"

    # chuẩn bị cho assistant trả lời
    prompt += "<|im_start|>assistant\n"

    return prompt

@app.post("/ask")
def ask(question : str):
    msgs = [
        {"role": "system", "content": "You are an assistant that converts physics problems into SMT-LIB formulas. Never compute numerical results. Only output declare-const, assert, and check-sat. Ignore irrelevant charges"},
        {"role": "user", "content": question }
    ]
    prompt = build_prompt(msgs)
    payload = {
        "model": "qwen3:8b",
        "prompt": prompt,
        "stream": False, 
        "keep_alive": 0
    }

    response = requests.post(OLLAMA_URL, json=payload)
    print(response.text)
    data = response.json()

    return {
        "answer": data["response"]
    }