import os
import uuid
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from http import HTTPStatus

UPLOAD_FOLDER = '/path/to/dir/'
ALLOWED_EXTENSIONS = {'webp', 'png', 'jpg', 'jpeg', 'gif', 'svg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify(error="No file part"), HTTPStatus.BAD_REQUEST

    file = request.files['file']

    if file.filename == '':
        return jsonify(error="No file name"), HTTPStatus.BAD_REQUEST

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_ext = filename.rsplit('.', 1)[1].lower()
        hash_filename = f"{uuid.uuid4().hex}.{file_ext}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], hash_filename))
        return jsonify(url=f"uploadsNew/{hash_filename}"), HTTPStatus.OK

    return jsonify(error="File not allowed"), HTTPStatus.BAD_REQUEST

if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=8989)
