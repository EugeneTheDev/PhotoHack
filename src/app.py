import flask
from flask import request
from flask import Flask
from src import text_analyze
from src import templates
import requests as re
from src.ThreadClass import RequestThread
import queue

app = Flask(__name__)
base_url = "/api"


@app.route(f"{base_url}/tonality", methods=["POST"])
def get_tonality():
    text = request.form["text"]
    if not text:
        return flask.jsonify({"success": False, "message": "String mustn't be empty"})
    emotion: dict = text_analyze.get_emotions(text)
    return flask.jsonify(emotion)


@app.route(f"{base_url}/upload", methods=["POST"])
def upload_info():

    file = request.files["upload"]
    img_url = re.post(url="http://upload-soft.photolab.me/upload.php?no_resize=1", files={
        "file": (file.filename, file.stream, file.mimetype)}).text
    if "http" not in img_url:
        return flask.jsonify({"success": False, "message": "Error with img sending"})

    urls_safe_queue = queue.Queue()
    threads = []

    for key in templates.templates.keys():
        thread = RequestThread(img_url, templates.templates[key], key, urls_safe_queue)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    formatted_emotions = dict({})

    for i in range(urls_safe_queue.qsize()):
        element = urls_safe_queue.get()
        for key in element.keys():
            if "http" not in element[key]:
                return flask.jsonify({"success": False, "message": "Error with img sending"})
            else:
                formatted_emotions.update(element)
    return flask.jsonify({"success": True, "emotions": formatted_emotions})

app.run()