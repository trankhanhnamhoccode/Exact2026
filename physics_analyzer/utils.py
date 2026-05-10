from pathlib import Path
from typing import Any, Dict
import json
import subprocess
import time


def load_prompt(filename: str, path: str = "prompts/", **kwargs) -> str:
    """
    Load prompt template and replace placeholders
    
    Args:
        filename: Name of the prompt file
        path: Directory path containing the prompt file
        **kwargs: Key-value pairs to replace {{key}} placeholders
    
    Returns:
        Filled prompt string
    """
    prompt_path = Path(path) / filename
    template = prompt_path.read_text(encoding="utf-8")
    
    # Replace placeholders
    for key, value in kwargs.items():
        placeholder = "{{" + key + "}}"
        template = template.replace(placeholder, value)
    
    return template


def start_ollama_server():
    """Start Ollama server in background"""
    # Kill existing ollama process if any
    subprocess.run("pkill ollama", shell=True, stderr=subprocess.DEVNULL)
    time.sleep(1)
    
    # Start ollama serve in background
    subprocess.Popen(
        "ollama serve", 
        shell=True, 
        stdout=subprocess.DEVNULL, 
        stderr=subprocess.DEVNULL
    )
    
    # Wait for server to start
    time.sleep(4)
    print("✅ Ollama server started successfully!")
    return True


def download_models(models: list):
    """
    Download required Ollama models
    
    Args:
        models: List of model names to download
    """
    import ollama
    
    for model in models:
        print(f"Downloading {model}...")
        ollama.pull(model)
        print(f"✅ {model} downloaded!")