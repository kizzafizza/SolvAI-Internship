from openai import OpenAI
from config import OPENAI_API_KEY, MODEL_NAME
from src.prompt_loader import load_prompt

client = OpenAI(api_key=OPENAI_API_KEY)


def generate_combined_report(
    student_profile: str,
    academic_result: str,
    academic_feedback: str
) -> str:
    base_prompt = load_prompt("combined_prompt.txt")

    full_prompt = f"""
{base_prompt}

Student profile notes:
{student_profile}

Academic result:
{academic_result}

Academic feedback:
{academic_feedback}
"""

    response = client.responses.create(
        model=MODEL_NAME,
        input=full_prompt
    )

    return response.output_text