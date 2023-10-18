from flask import Blueprint, send_from_directory, render_template_string
from config import settings
import os

file_explorer_bp = Blueprint('file_explorer', __name__)

@file_explorer_bp.route('/', defaults={'req_path': ''})
@file_explorer_bp.route('/<path:req_path>')
def dir_listing(req_path):
    abs_path = os.path.join(settings.SAVE_DIRECTORY, req_path)

    # Return 404 if path doesn't exist
    if not os.path.exists(abs_path):
        return "Not found", 404

    # Check if path is a file and serve
    if os.path.isfile(abs_path):
        return send_from_directory(settings.SAVE_DIRECTORY, req_path, as_attachment=True)

    # Parse files from os.listdir and dont display anything that isn't either archive or railway
    files_and_types = [
        {'name': f, 'is_directory': os.path.isdir(os.path.join(abs_path, f))}
        for f in os.listdir(abs_path)
        if f == "archive" or f.startswith("railway")
    ]
    return render_template_string(settings.DIRECTORY_TEMPLATE, files=files_and_types, req_path=req_path)