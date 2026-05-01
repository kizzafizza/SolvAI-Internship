from openai import OpenAI
from config import OPENAI_API_KEY, MODEL_NAME
from src.prompt_loader import load_prompt
import json

client = OpenAI(api_key=OPENAI_API_KEY)

def evaluate_feedback(question: str, expected_answer: str, student_answer: str, generated_feedback: str) -> dict:

    evaluation_prompt = load_prompt("evaluation_prompt.txt")

    full_prompt = f"""
    {evaluation_prompt}

    Question:
    {question}

    Expected answer:
    {expected_answer}

    Student answer:
    {student_answer}

    AI-generated feedback:
    {generated_feedback}
    """

    response = client.responses.create(
        model=MODEL_NAME,
        input=full_prompt
    )

    output_text = response.output_text
    #print("RAW:", output_text)
    return json.loads(output_text)
