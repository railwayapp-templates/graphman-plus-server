from flask import Flask
from explorer.routes import file_explorer_bp
from upload.routes import upload_file_bp
import os

app = Flask(__name__)

app.register_blueprint(file_explorer_bp)
app.register_blueprint(upload_file_bp)


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
