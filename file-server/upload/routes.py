from flask import Blueprint, request, jsonify
from utils.handleFile import handleFile

upload_file_bp = Blueprint('upload_file', __name__)

@upload_file_bp.route('/upload', methods=['POST'])
def upload_file():
    print('Request received, checking file.')
    data = request.json
    result = handleFile(data)
    if result > 0:
        return jsonify({"message": "File saved successfully!"}), 200
    else:
        return jsonify({"message": "No changes detected"}), 200