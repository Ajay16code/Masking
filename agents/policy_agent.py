import re

class PolicyAgent:
    def __init__(self):
        self.name = "PolicyAgent"
        self.SSN_REGEX = re.compile(r"\b\d{3}[- ]?\d{2}[- ]?\d{4}\b")
        self.DATE_REGEX = re.compile(r"\b(?:\d{1,2}[\-/]){2}\d{2,4}\b")

    def process(self, text_data, rules):
        """
        Analyzes text data and applies masking rules.
        Returns: { 'regions': list, 'log': str }
        """
        log = []
        regions = []
        log.append(f"[{self.name}] Analyzing text against rules: {rules}...")

        if not text_data:
            log.append(f"[{self.name}] No text data to analyze.")
            return {'regions': [], 'log': log}

        n = len(text_data['text'])
        counts = {"SSN": 0, "DOB": 0, "NAME": 0}

        for i in range(n):
            text = (text_data['text'][i] or "").strip()
            if not text:
                continue

            label = None
            if "SSN" in rules and self.SSN_REGEX.search(text):
                label = "SSN"
            elif "DOB" in rules and self.DATE_REGEX.search(text):
                label = "DOB"
            elif "NAME" in rules and (text.isalpha() and text.isupper() or text.istitle()):
                 # Simple heuristic: ignore small words to avoid over-masking common words
                if len(text) > 2: 
                    label = "NAME"

            if label:
                counts[label] += 1
                regions.append({
                    'x': text_data['left'][i],
                    'y': text_data['top'][i],
                    'w': text_data['width'][i],
                    'h': text_data['height'][i],
                    'label': label
                })

        log.append(f"[{self.name}] Identification complete.")
        log.append(f"[{self.name}] Found {counts['SSN']} SSNs, {counts['DOB']} DOBs, {counts['NAME']} Names to redact.")
        
        return {'regions': regions, 'log': log}
