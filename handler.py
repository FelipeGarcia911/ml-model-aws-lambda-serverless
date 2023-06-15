import json
from app.http.index import predict_regresion

def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "response": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def predict(event, context):
    result = predict_regresion(event)

    body = {
        "message": "Prediction executed successfully!",
        "response": result
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response