from flask import Flask, request
from flask import jsonify
from models.predict import Predict
import json


def create_app():
    app = Flask(__name__)
    return app


app = create_app()


@app.route("/api/v1/hello", methods=["GET"])
def hello():
    response = {"message": "Hello from the API"}

    return jsonify(response)


@app.route("/api/v1/predict", methods=["POST"])
def predict():
    response = {"message": "error"}
    content_type = request.headers.get("Content-Type")
    if content_type == "application/json":
        payload = request.get_json(force=True)
        predict = Predict.getPrediction(payload)
        response = {"message": "success", "predict": predict}
    else:
        response = {"message": "Content-Type not supported!"}

    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
