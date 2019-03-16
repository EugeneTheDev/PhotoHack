<<<<<<< HEAD
from flask import Flask, request
import requests
=======
import flask
from flask import request
from flask import Flask

app = Flask(__name__)
base_url = "/api"

def textAnalyze():



# @app.route(f"{base_url}/upload", methods=["POST"])
# def upload_info():
#     request.files["upload"].save("./static/image.png")
#     print(request.form["text"])
#     return flask.jsonify({
#         "message": "Successfully uploaded"
#     })

@app.route('/stream_file', methods=["POST"])
def stream_file():
    file = request.files['file']
    sendFile = {"file": (file.filename, file.stream, file.mimetype)}
    r = requests.post("http://myservicedotcom/upload", files=sendFile)

