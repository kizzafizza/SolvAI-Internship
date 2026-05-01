from openai import OpenAI
from config import OPENAI_API_KEY, MODEL_NAME
from src.prompt_loader import load_prompt

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_feedback(question: str, expected_answer: str, student_answer: str) -> str:
    base_prompt = load_prompt("feedback_prompt.txt")

    full_prompt = f"""
{base_prompt}

Question:
{question}

Expected answer:
{expected_answer}

Student answer:
{student_answer}
"""

    response = client.responses.create(
        model=MODEL_NAME,
        input=full_prompt
    )

    return response.output_text