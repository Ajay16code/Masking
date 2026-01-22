from models.llm_client import ask_llm

def decide_masking_strategy(analysis):
    prompt = f"""
    Given the detected text: {analysis['text']}

    Decide:
    1. What fields to mask (SSN, DOB, NAME)
    2. Masking type (blur / block)

    Return JSON only.
    """

    decision = ask_llm(prompt)
    return decision
