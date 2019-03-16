import requests as re
import flask
from flask import request
from flask import Flask
from flask import Response

from src import text_analyze
from src import templates

app = Flask(__name__)
base_url = "/api"


@app.route(f"{base_url}/upload", methods=["POST"])
def upload_info():
    file = request.files["upload"]
    text = request.form["text"]
    emotion = text_analyze.get_emotions(text)
    img_url = re.post(url="http://upload-soft.photolab.me/upload.php?no_resize=1", files={
        "file": (file.filename, file.stream, file.mimetype)}).text

    result_url = re.post(url="http://api-soft.photolab.me/template_process.php", data={
        "image_url[1]": img_url,
        "template_name": templates.templates["anger"]  # hardcoded
    }).text
    return result_url
