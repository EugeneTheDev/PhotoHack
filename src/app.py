import requests as re
import flask
from flask import request
from flask import Flask
from flask import Response

app = Flask(__name__)
base_url = "/api"


@app.route(f"{base_url}/upload", methods=["POST"])
def upload_info():
    file = request.files["upload"]
    text = request.form["text"]
    emotion = ""

    img_url = re.post(url="http://upload-soft.photolab.me/upload.php?no_resize=1", files={
        "file": (file.filename, file.stream, file.mimetype)}).text

    result_url = re.post(url="http://api-soft.photolab.me/template_process.php", data={
        "image_url[1]": img_url,
        "template_name": "1668"  # hardcoded
    }).text
    result = re.get(result_url, stream=True)
    return Response(flask.stream_with_context(result.iter_content()), content_type=result.headers['content-type'])

# @app.route('/stream_file', methods=["POST"])
# def stream_file():
#     file = request.files['file']
#     send_file = {"file": (file.filename, file.stream, file.mimetype)}
#     r = requests.post("http://myservicedotcom/upload", files=sendFile)
#
# # app.run()


get_emotions('i am so fucking happy')