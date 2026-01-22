from agents.analysis_agent import analyze_image
from agents.decision_agent import decide_masking_strategy
from agents.masking_agent import apply_mask
from agents.quality_agent import verify_mask
from agents.action_agent import save_result

def run_agent_pipeline(image, output_path):
    analysis = analyze_image(image)
    decision = decide_masking_strategy(analysis)

    # Dummy box (replace with real OCR boxes)
    boxes = [(50,50,200,60)]

    masked = apply_mask(image, boxes)

    if verify_mask(masked):
        return save_result(masked, output_path)

    return None
