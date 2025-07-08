from flask import Flask, request, jsonify, send_from_directory, send_file
from flask_cors import CORS
from database import init_db, insert_image, get_image_by_id, update_classification, get_latest_image_id
from utils import decode_base64_string, classify_image
import os
from pathlib import Path

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

init_db()

# Get the path to the frontend directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent
FRONTEND_DIR = os.path.join(PROJECT_ROOT, "frontend")

@app.route('/')
def home():
    """Serve the main frontend page"""
    return send_file(os.path.join(FRONTEND_DIR, "index.html"))

@app.route('/<path:filename>')
def serve_static(filename):
    """Serve static files from frontend directory"""
    return send_from_directory(FRONTEND_DIR, filename)

@app.route('/predict', methods=['POST'])
def predict():
    image_data = request.json.get('image_data')
    image_binary = decode_base64_string(image_data)
    insert_image(image_binary)
    latest_id = get_latest_image_id()
    stored_image = get_image_by_id(latest_id)[1]
    classification_result = classify_image(stored_image)
    update_classification(latest_id, classification_result['class'])
    return jsonify(classification_result)




if __name__ == '__main__':
    app.run(port=5000, debug=True)