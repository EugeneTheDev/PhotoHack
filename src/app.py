import flask
from flask import request
from flask import Flask

app = Flask(__name__)
base_url = "/api"


@app.route(f"{base_url}/upload", methods=["POST"])
def upload_info():
    request.files["upload"].save("./static/image.png")
    print(request.form["text"])
    return flask.jsonify({
        "message": "Successfully uploaded"
    })


