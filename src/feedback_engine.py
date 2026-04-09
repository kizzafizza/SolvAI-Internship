from openai import OpenAI
from config import OPENAI_API_KEY, MODEL_NAME
from src.prompt_loader import load_prompt

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_feedback(student_answer: str) -> str:
    base_prompt = load_prompt("feedback_prompt.txt")

    full_prompt = f"""
{base_prompt}

Student answer:
{student_answer}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are an educational feedback assistant."},
            {"role": "user", "content": full_prompt},
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content