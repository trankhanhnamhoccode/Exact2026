#!/usr/bin/env python3
"""
Physics Problem Classifier and Extractor
Main script to run the problem analysis pipeline
"""

import json
from ollama import generate
from pydantic import BaseModel
from typing import Dict, Any
from utils import load_prompt, start_ollama_server, download_models


class ClassificationResponse(BaseModel):
    qtype: str


class ExtractionResponse(BaseModel):
    given: list
    unknown: list
    topology: str
    problem_type: str
    difficulty: int


def classify_with_llm(question: str, model: str = "qwen3:0.6b") -> Dict[str, Any]:
    """
    Classify question as physics or logic
    
    Args:
        question: The question to classify
        model: Ollama model to use
    
    Returns:
        Dictionary with classification result
    """
    prompt_text = load_prompt(
        filename="prompt.txt",
        path="prompts/",
        QUESTION="QUESTION: " + question
    )
    
    response = generate(
        model=model,
        prompt=prompt_text,
        options={
            'temperature': 0,
            'stream': False,
            'format': ClassificationResponse.model_json_schema(),
            'keep_alive': '5m',
            'num_predict': 1000
        }
    )
    
    return json.loads(response['response'])


def problem_extracter(question: str, model: str = "qwen3:1.7b") -> Dict[str, Any]:
    """
    Extract physics problem details
    
    Args:
        question: The physics question to analyze
        model: Ollama model to use (larger model for better extraction)
    
    Returns:
        Dictionary with extracted problem information
    """
    prompt_text = load_prompt(
        filename="physicPrompt.txt",
        path="prompts/",
        QUESTION="QUESTION: " + question
    )
    
    response = generate(
        model=model,
        prompt=prompt_text,
        options={
            'temperature': 0,
            'stream': False,
            'format': ExtractionResponse.model_json_schema(),
            'keep_alive': '5m',
            'num_predict': 6000
        }
    )
    
    return json.loads(response['response'])


def main():
    """Main function to run the pipeline"""
    
    # Start Ollama server
    print("Starting Ollama server...")
    start_ollama_server()
    
    # Download required models
    print("\nDownloading models...")
    models_to_download = [
        "qwen3:0.6b",
        "qwen3:1.7b",
        "qwen3:4b"
    ]
    download_models(models_to_download)
    
    # Test questions
    test_questions = {
        "q1": "Two electric charges q1 = +9×10⁻⁶ C and q2 = -9×10⁻⁶ C are placed 10 cm apart. A charge q3 = +9×10⁻⁶ C is at the midpoint. Bring the problem to SMT formula to find forces between q1 and q3",
        
        "q2": "Calculate the energy stored in capacitor C when C = 100 μF and U = 30 V.",
        
        "q3": "An object undergoes simple harmonic motion with the equation x = 4cos(2πt + π/2) cm. Determine the amplitude, period, and initial position of the object.",
        
        "q4": "A 5 kg block on a frictionless 30° incline is connected to a 3 kg hanging mass by a string over a pulley. Find the acceleration and the tension in the string.",
        
        "q5": "A car accelerates uniformly from rest to 20 m/s in 8 seconds. It then accelerates again at 1.5 m/s² for 6 seconds. Calculate the final velocity of the car and the total distance traveled."
    }
    
    print("\n" + "="*60)
    print("PHYSICS PROBLEM ANALYZER")
    print("="*60)
    
    # Test classification
    print("\n📋 CLASSIFICATION TESTS")
    print("-" * 40)
    
    for name, question in test_questions.items():
        print(f"\nQuestion {name}: {question[:80]}...")
        try:
            classification = classify_with_llm(question)
            print(f"  Type: {classification['qtype']}")
        except Exception as e:
            print(f"  Error: {e}")
    
    # Test extraction on physics questions
    print("\n\n🔬 PROBLEM EXTRACTION TESTS")
    print("-" * 40)
    
    physics_questions = [test_questions["q3"], test_questions["q4"], test_questions["q5"]]
    
    for i, question in enumerate(physics_questions, 1):
        print(f"\nTest {i}: {question[:80]}...")
        try:
            extraction = problem_extracter(question)
            print(f"  Problem Type: {extraction.get('problem_type', 'N/A')}")
            print(f"  Topology: {extraction.get('topology', 'N/A')}")
            print(f"  Difficulty Level: {extraction.get('difficulty', 'N/A')}")
            print(f"  Known variables: {len(extraction.get('given', []))}")
            print(f"  Unknown variables: {len(extraction.get('unknown', []))}")
        except Exception as e:
            print(f"  Error: {e}")


if __name__ == "__main__":
    main()