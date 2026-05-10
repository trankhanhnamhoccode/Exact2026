#!/usr/bin/env python3
"""
Quick test script - run individual questions without full setup
"""

import json
from ollama import generate
from utils import load_prompt, start_ollama_server


def test_single_question(question: str, mode: str = "classify"):
    """
    Test a single question
    
    Args:
        question: The question to analyze
        mode: Either "classify" or "extract"
    """
    
    if mode == "classify":
        prompt_text = load_prompt(
            filename="prompt.txt",
            path="prompts/",
            QUESTION="QUESTION: " + question
        )
        
        response = generate(
            model='qwen3:0.6b',
            prompt=prompt_text,
            options={
                'temperature': 0,
                'stream': False,
                'num_predict': 1000
            }
        )
        
        print("Classification:", response['response'])
    
    elif mode == "extract":
        prompt_text = load_prompt(
            filename="physicPrompt.txt",
            path="prompts/",
            QUESTION="QUESTION: " + question
        )
        
        response = generate(
            model='qwen3:1.7b',
            prompt=prompt_text,
            options={
                'temperature': 0,
                'stream': False,
                'num_predict': 6000
            }
        )
        
        # Try to parse as JSON
        try:
            result = json.loads(response['response'])
            print(json.dumps(result, indent=2, ensure_ascii=False))
        except:
            print("Raw response:", response['response'])


if __name__ == "__main__":
    # Start server if not running
    start_ollama_server()
    
    # Test with a simple question
    test_question = "A 2 kg object is moving at 5 m/s. Calculate its kinetic energy."
    
    print("Testing classification:")
    test_single_question(test_question, "classify")
    
    print("\n" + "="*50)
    
    print("Testing extraction:")
    physics_question = "A 5 kg block on a 30° incline is connected to a 3 kg hanging mass. Find acceleration."
    test_single_question(physics_question, "extract")