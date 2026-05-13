from openai import OpenAI
from config import OPENAI_API_KEY, MODEL_NAME
from src.prompt_loader import load_prompt

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_profile_comment(student_name: str, student_profile: str, expected_focus: str) -> str:
    base_prompt = load_prompt("profile_prompt.txt")

    full_prompt = f"""
{base_prompt}

Student name:
{student_name}

Student profile notes:
{student_profile}

Expected focus:
{expected_focus}
"""

    response = client.responses.create(
        model=MODEL_NAME,
        input=full_prompt
    )

    return response.output_text