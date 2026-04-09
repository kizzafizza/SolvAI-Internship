from pathlib import Path

def load_prompt(filename: str) -> str:
    """
    Load a prompt file from the prompts directory.
    """
    prompts_dir = Path(__file__).resolve().parent.parent / "prompts"
    prompt_path = prompts_dir / filename

    if not prompt_path.exists():
        raise FileNotFoundError(f"Prompt file not found: {prompt_path}")

    return prompt_path.read_text(encoding="utf-8")