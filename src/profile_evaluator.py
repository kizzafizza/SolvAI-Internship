import json
from openai import OpenAI
from config import OPENAI_API_KEY, MODEL_NAME
from src.prompt_loader import load_prompt

client = OpenAI(api_key=OPENAI_API_KEY)

def evaluate_profile_comment(student_profile: str, expected_focus: str, generated_comment: str) -> dict:
    evaluation_prompt = load_prompt("profile_evaluation_prompt.txt")

    full_prompt = f"""
{evaluation_prompt}

Student profile notes:
{student_profile}

Expected focus:
{expected_focus}

AI-generated student profile comment:
{generated_comment}
"""

    response = client.responses.create(
        model=MODEL_NAME,
        input=full_prompt
    )

    output_text = response.output_text

    try:
        return json.loads(output_text)
    except json.JSONDecodeError:
        return {
            "profile_alignment": 0,
            "tone_professionalism": 0,
            "specificity": 0,
            "constructiveness": 0,
            "sensitivity": 0,
            "summary": f"Invalid JSON returned: {output_text}"
        }