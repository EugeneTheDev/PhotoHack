import requests
from flask import jsonify
from flask import request
from flask import Flask
import json
app = Flask(__name__)
base_url = "/api"



# @app.route(f"{base_url}/upload", methods=["POST"])
# def upload_info():
#     request.files["upload"].save("./static/image.png")
#     print(request.form["text"])
#     return flask.jsonify({
#         "message": "Successfully uploaded"
#     })


# @app.route('/stream_file', methods=["POST"])
# def stream_file():
#     file = request.files['file']
#     send_file = {"file": (file.filename, file.stream, file.mimetype)}
#     r = requests.post("http://myservicedotcom/upload", files=sendFile)
#
# # app.run()


get_emotions('i am so fucking happy')