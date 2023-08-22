from flask import Flask, request
from flask import jsonify
from predict.main import Predict
from gevent.pywsgi import WSGIServer
from dotenv import dotenv_values

config = dotenv_values(".env")

PORT = int(config.get("PORT", 10000))
ENVIRONMENT = config.get("ENVIRONMENT", "production")


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
        result = Predict.getPrediction(payload)
        response = {"message": "success", "prediction": result}
    else:
        response = {"message": "Content-Type not supported!"}

    return jsonify(response)


if __name__ == "__main__":
    print("Server starting at PORT={0} and MODE={1}".format(PORT, ENVIRONMENT))
    if ENVIRONMENT == "production":
        http_server = WSGIServer(
            ("", PORT),
            app,
        )
        http_server.serve_forever()
    else:
        app.run(host="0.0.0.0", port=PORT, debug=True)
