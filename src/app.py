import flask
from flask import request
from flask import Flask
from src import text_analyze
from src import templates
import requests as re

app = Flask(__name__)
base_url = "/api"

@app.route(f"{base_url}/tonality", methods=["POST"])
def get_tonality():
    text = request.form["text"]
    if not text:
        return flask.jsonify({"success": False, "message": "String mustn't be empty"})
    emotion: dict = text_analyze.get_emotions(f" {text} "*10)
    return flask.jsonify(emotion)


@app.route(f"{base_url}/upload/<emotion>", methods=["POST"])
def upload_info(emotion):
    file = request.files["upload"]
    print(templates.templates.keys())
    if emotion not in templates.templates:
        return flask.jsonify({"success": False, "message": "There is no such an emotion"})
    else:
        template = templates.templates[emotion]
    img_url = re.post(url="http://upload-soft.photolab.me/upload.php?no_resize=1", files={
        "file": (file.filename, file.stream, file.mimetype)}).text
    if "http" not in img_url:
        return flask.jsonify({"success": False, "message": "Error with img sending"})
    result_url = re.post(url="http://api-soft.photolab.me/template_process.php", data={
        "image_url[1]": img_url,
        "template_name": template
    }).text
    if "http" not in result_url:
        return flask.jsonify({"success": False, "message": "Error with img sending"})
    return flask.jsonify({"success": True, "url": result_url})
