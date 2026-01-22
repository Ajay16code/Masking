import os
import cv2
import numpy as np
from flask import Flask, request, render_template, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename

# Agents
from agents.orchestrator import Orchestrator
from utils.file_handler import ensure_dir

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(APP_ROOT, "static", "uploads")
RESULT_DIR = os.path.join(APP_ROOT, "static", "results")

# Initialize
ensure_dir(UPLOAD_DIR)
ensure_dir(RESULT_DIR)

app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = "dev-secret"

# Initialize Orchestrator
orchestrator = Orchestrator()

ALLOWED_IMG = {"png", "jpg", "jpeg"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_IMG

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    file_img = request.files.get("image")
    # Get checkboxes (optional now if mission is used)
    hide_types = request.form.getlist("rules") 
    # Get mission prompt
    mission_prompt = request.form.get("mission", "").strip()

    if not file_img or not allowed_file(file_img.filename):
        flash("Invalid or missing image file")
        return redirect(url_for("index"))

    # Logic: Either checkboxes OR mission must be present
    if not hide_types and not mission_prompt:
        flash("Please select an option or enter a mission directive.")
        return redirect(url_for("index"))

    img_name = secure_filename(file_img.filename)
    img_path = os.path.join(UPLOAD_DIR, img_name)
    file_img.save(img_path)

    # Process
    img = cv2.imread(img_path)
    if img is None:
        flash("Failed to read image")
        return redirect(url_for("index"))

    # Use Orchestrator with mission prompt
    try:
        result = orchestrator.run_pipeline(img, hide_types, mission_prompt=mission_prompt)
        masked_img = result['masked_image']
        logs = result['logs']
    except Exception as e:
        flash(f"An internal agent error occurred: {str(e)}")
        return redirect(url_for("index"))

    out_name = f"masked_{img_name}"
    out_path = os.path.join(RESULT_DIR, out_name)
    cv2.imwrite(out_path, masked_img)

    result_url = url_for('static', filename=f"results/{out_name}")
    
    # Render with logs and filename for download
    return render_template("index.html", result_url=result_url, logs=logs, result_filename=out_name)

@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory(RESULT_DIR, filename, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
