from flask import Flask, request
import requests
app = Flask(__name__)


@app.route('/stream_file', methods=["POST"])
def stream_file():
    file = request.files['file']
    sendFile = {"file": (file.filename, file.stream, file.)}


app.run()