from agents.analysis_agent import AnalysisAgent
from agents.policy_agent import PolicyAgent
from agents.masking_agent import RedactionAgent
from agents.audit_agent import AuditAgent
from agents.vision_agent import VisionAgent
from agents.reasoning_agent import ReasoningAgent

class Orchestrator:
    def __init__(self):
        self.analysis_agent = AnalysisAgent()
        self.policy_agent = PolicyAgent()
        self.redaction_agent = RedactionAgent()
        self.audit_agent = AuditAgent()
        self.vision_agent = VisionAgent()
        self.reasoning_agent = ReasoningAgent()

    def run_pipeline(self, image, rules, mission_prompt=""):
        """
        Executes the agentic workflow.
        Returns: { 'masked_image': img, 'logs': list }
        """
        full_logs = []
        full_logs.append("[Orchestrator] Pipeline initialized. Deploying agents...")
        
        # 0. Reasoning (Cognitive Layer)
        enable_vision = False
        if mission_prompt:
             res_reasoning = self.reasoning_agent.process(mission_prompt, rules)
             full_logs.extend(res_reasoning['log'])
             rules = res_reasoning['updated_rules']
             enable_vision = res_reasoning['enable_vision']
        
        # 1. Vision (Visual Layer) - Parallel to Analysis
        vision_regions = []
        if enable_vision:
            res_vision = self.vision_agent.process(image)
            full_logs.extend(res_vision['log'])
            vision_regions = res_vision['regions']

        # 2. Analysis (Text Layer)
        res_analysis = self.analysis_agent.process(image)
        full_logs.extend(res_analysis['log'])
        text_data = res_analysis['text_data']

        if not text_data:
             full_logs.append("[Orchestrator] Pipeline aborted: text analysis failed.")
             return {'masked_image': image, 'logs': full_logs}

        # 2. Policy
        res_policy = self.policy_agent.process(text_data, rules)
        full_logs.extend(res_policy['log'])
        regions = res_policy['regions']
        
        # Merge Text Regions + Vision Regions
        all_regions = regions + vision_regions

        # 4. Redaction
        res_redaction = self.redaction_agent.process(image, all_regions)
        full_logs.extend(res_redaction['log'])
        masked_image = res_redaction['masked_image']

        # 5. Audit
        res_audit = self.audit_agent.process(len(all_regions), len(all_regions))
        full_logs.extend(res_audit['log'])

        full_logs.append("[Orchestrator] Process complete. Secure output generated.")
        
        return {
            'masked_image': masked_image, 
            'logs': full_logs
        }
