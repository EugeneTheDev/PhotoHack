import flask
from flask import request
from flask import Flask
from src.ThreadClass import RequestThread
from src import text_analyze
from src import templates
import queue

app = Flask(__name__)
base_url = "/api"


@app.route(f"{base_url}/upload", methods=["POST"])
def upload_info():
    file = request.files["upload"]
    urls_safe_queue = queue.Queue()
    threads = []

    for temp_name in templates.templates.keys():
        thread = RequestThread(file, templates.templates[temp_name], temp_name,urls_safe_queue)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    emotion_results = dict({})
    for i in range(urls_safe_queue.qsize()):
        emotion_results.update(urls_safe_queue.get())

    return flask.jsonify({"success": True, "emotions": emotion_results})


@app.route(f"{base_url}/tonality", methods=["POST"])
def get_tonality():
    text = request.form["text"]
    if not text:
        return flask.jsonify({"success": False, "message": "String mustn't be empty"})
    emotion: dict = text_analyze.get_emotions(text)
    return flask.jsonify(emotion)



app.run()

