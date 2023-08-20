import json

import pandas as pd
from tensorflow import keras

model_path = "./src/http/regresion-model.keras"
model = keras.models.load_model(model_path)

column_names = ['Cylinders','Displacement','Horsepower','Weight', 'Acceleration', 'Model Year', 'USA', 'Europe', 'Japan']

def predict_regresion(event):
    items = json.loads(event)
    dataset = pd.DataFrame([items], columns=column_names)
    prediction = model.predict(dataset).flatten()

    return 'The predicted value is: ' + str(prediction[0]) + ' MPG'
