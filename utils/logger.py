import json

def log_event(data):
    with open("memory/agent_logs.json", "a") as f:
        f.write(json.dumps(data) + "\n")
