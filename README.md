
# Masking Tool – Agentic AI

An Agentic AI–based image masking system that automatically detects sensitive information, applies masking, and verifies output quality using a multi-agent decision pipeline. The project is designed for privacy-preserving image and document processing.

---

## Overview

This system uses a coordinated set of AI agents to analyze images, make masking decisions, apply visual obfuscation, and validate results. The architecture follows agentic AI principles with reasoning, policy enforcement, memory, and auditing.

The application is exposed through a web interface built with Flask, allowing users to upload images and receive verified masked outputs.

---

## Key Capabilities

- Multi-agent orchestration for image analysis and masking
- Face detection using classical computer vision
- OCR and segmentation model support (extensible)
- Policy-based masking decisions
- Quality validation before output delivery
- Agent memory and audit logging
- Web-based user interface

---

## Agent Architecture

The system is built around specialized agents, each with a focused responsibility:

- Vision Agent: Detects faces and visual regions of interest
- Analysis Agent: Interprets detection results
- Policy Agent: Applies masking rules and compliance logic
- Decision Agent: Determines masking strategy
- Masking Agent: Applies blur or region masking
- Quality Agent: Verifies masking completeness
- Audit Agent: Logs decisions and actions
- Reasoning Agent: Maintains contextual reasoning
- Orchestrator: Coordinates agent execution flow
- Controller: Entry point for agent pipeline execution

---

## Project Structure

```

Masking/
│
├── agents/
│   ├── action_agent.py
│   ├── analysis_agent.py
│   ├── audit_agent.py
│   ├── controller.py
│   ├── decision_agent.py
│   ├── masking_agent.py
│   ├── orchestrator.py
│   ├── policy_agent.py
│   ├── quality_agent.py
│   ├── reasoning_agent.py
│   ├── vision_agent.py
│   └── **init**.py
│
├── config/
│   ├── config.py
│   └── settings.py
│
├── memory/
│   ├── agent_logs.json
│   ├── decision_history.json
│   └── feedback_store.json
│
├── models/
│   ├── llm_client.py
│   ├── ocr_model.py
│   └── segmentation_model.py
│
├── services/
│   ├── image_service.py
│   ├── masking_service.py
│   └── validation_service.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── uploads/
│   ├── masked_outputs/
│   └── results/
│
├── templates/
│   ├── index.html
│   ├── dashboard.html
│   └── result.html
│
├── tests/
│   ├── test_agents.py
│   └── test_pipeline.py
│
├── utils/
│   ├── file_handler.py
│   ├── helpers.py
│   └── logger.py
│
├── app.py
├── haarcascade_frontalface_default.xml
├── requirements.txt
├── .gitignore
└── README.md

````

---

## Technology Stack

- Python 3.12
- Flask (backend framework)
- OpenCV (computer vision)
- HTML and CSS (frontend)
- Agentic AI design pattern

---

## Installation

### Clone the Repository
```bash
git clone https://github.com/Ajay16code/Masking.git
cd Masking
````

### Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

```bash
python app.py
```

Open the browser and navigate to:

```
http://127.0.0.1:5000
```

---

## Application Workflow

1. User uploads an image through the web interface
2. Vision Agent detects sensitive regions
3. Analysis and Policy Agents evaluate findings
4. Decision Agent selects masking strategy
5. Masking Agent applies obfuscation
6. Quality Agent verifies output integrity
7. Audit Agent records all actions
8. Final masked image is displayed to the user

---

## Security and Privacy

* Environment variables are excluded using `.gitignore`
* Uploaded images are not permanently stored
* All agent actions are logged for auditability
* Designed with privacy-by-design principles

---

## Testing

Run unit and pipeline tests using:

```bash
pytest tests/
```

---

## Future Improvements

* Deep learning–based face and object detection
* OCR-based document text masking
* Video masking pipeline
* Dockerized deployment
* Role-based access control
* Cloud and API integration

---

## License

This project is licensed under the MIT License.

---

## Author

Ajay
GitHub: [https://github.com/Ajay16code](https://github.com/Ajay16code)

```

