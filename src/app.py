from flask import Flask, request
import requests
app = Flask(__name__)

def textAnalyze():



@app.route('/stream_file', methods=["POST"])
def stream_file():
    file = request.files['file']
    sendFile = {"file": (file.filename, file.stream, file.mimetype)}
    r = requests.post("http://myservicedotcom/upload", files=sendFile)

