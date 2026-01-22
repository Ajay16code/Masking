import re

class ReasoningAgent:
    def __init__(self):
        self.name = "ReasoningAgent"
        
        # --- KNOWLEDGE BASE (50+ Variations) ---
        self.keywords = {
            "NAME": [
                "name", "names", "fullname", "full name", "surname", "lastname", "last name",
                "firstname", "first name", "middle name", "initials", "person", "persons",
                "people", "individual", "individuals", "identity", "identities", "who", "whom",
                "employee", "client", "customer", "patient", "student", "applicant", "suspect",
                "victim", "witness", "holder", "owner", "buyer", "seller", "signatory", "alias",
                "aka", "pseudonym", "title", "designation", "role", "character", "actor", "subject",
                "entity", "entities", "member", "staff", "manager", "director", "ceo", "founder"
            ],
            "SSN": [
                "ssn", "social security", "social-security", "socialsecurity", "soc sec", "soc-sec",
                "s.s.n", "id number", "id #", "tax id", "tin", "ein", "national id", "govt id",
                "government id", "federal id", "personal id", "identification number", "social number",
                "insurance number", "policy number", "account number", "reference number", "ref number",
                "case number", "serial number", "badge number", "license number", "permit number"
            ],
            "DOB": [
                "dob", "date of birth", "birth date", "birthday", "birthdate", "born on", "born",
                "age", "dates", "date", "year", "month", "day", "calendar", "timeline", "timestamp",
                "when", "time", "duration", "period", "era", "epoch", "anniversary", "jubilee"
            ],
            "VISION": [
                "face", "faces", "photo", "photos", "picture", "pictures", "image", "images",
                "headshot", "portrait", "mugshot", "selfie", "visage", "appearance", "look",
                "visual", "snapshot", "pic", "pics", "avatar", "profile pic", "profile picture"
            ]
        }

    def process(self, prompt, active_rules):
        """
        Analyzes the mission objective and updates active rules.
        Returns: { 'updated_rules': list, 'enable_vision': bool, 'log': list }
        """
        log = []
        log.append(f"[{self.name}] Analysis Module Active. Parsing Directive: \"{prompt}\"")
        
        updated_rules = list(active_rules)
        enable_vision = False
        
        prompt_lower = prompt.lower()
        
        # Logic 1: Exclusivity Check ("only", "just", "nothing else")
        is_exclusive = any(x in prompt_lower for x in ["only", "just", "solely", "exclusively"])
        if is_exclusive:
             log.append(f"[{self.name}] Exclusivity Constraint Detected ('only'). Resetting default protocols.")
             updated_rules = [] # Reset to build from scratch
        
        # Logic 2: Keyword Matching
        matches_found = []
        
        # Check NAMES
        if any(w in prompt_lower for w in self.keywords["NAME"]):
            if "NAME" not in updated_rules:
                updated_rules.append("NAME")
                matches_found.append("NAME")
        
        # Check SSN
        if any(w in prompt_lower for w in self.keywords["SSN"]):
            if "SSN" not in updated_rules:
                updated_rules.append("SSN")
                matches_found.append("SSN")

        # Check DOB
        if any(w in prompt_lower for w in self.keywords["DOB"]):
            if "DOB" not in updated_rules:
                updated_rules.append("DOB")
                matches_found.append("DOB")
                
        # Check VISION (Faces)
        if any(w in prompt_lower for w in self.keywords["VISION"]) or "face" in prompt_lower:
             enable_vision = True
             matches_found.append("VISION_PROTOCOL")

        # Logic 3: "All" / "Everything" override
        if any(x in prompt_lower for x in ["all", "everything", "everything", "complete", "full", "total"]):
             if not is_exclusive: # "All names only" should be treated as Names only
                 # Ambiguity check: "All names" -> Names. "Mask everything" -> All.
                 # Heuristic: If specific categories matched, trust those. If NO categories matched but "all" is present, enable everything.
                 if not matches_found: 
                     updated_rules = ["SSN", "DOB", "NAME"]
                     enable_vision = True
                     log.append(f"[{self.name}] 'OMEGA' Protocol: All security measures enabled by blanket request.")
        
        # Logging results
        if matches_found:
            log.append(f"[{self.name}] Intent Decoded. Active Protocols: {', '.join(matches_found)}.")
        else:
            if not updated_rules and not enable_vision:
                 log.append(f"[{self.name}] No specific protocols identified in directive. Maintaining current state.")

        return {
            'updated_rules': updated_rules,
            'enable_vision': enable_vision,
            'log': log
        }
