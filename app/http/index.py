from io import StringIO
import pandas as pd
import json
import joblib

model = joblib.load('./app/trained/regresion-model.joblib')
column_names = ['Cylinders','Displacement','Horsepower','Weight', 'Acceleration', 'Model Year', 'USA', 'Europe', 'Japan']

def predict_regresion(event):
    items = json.loads(event)
    dataset = pd.DataFrame([items], columns=column_names)
    prediction = model.predict(dataset).flatten()

    return 'The predicted value is: ' + str(prediction[0]) + ' MPG'
