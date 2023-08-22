from tensorflow import keras
import pandas as pd


model_path = "./src/app/routes/regresion_mpg/model.keras"

class MPGPrediction:
    model = keras.models.load_model(model_path)
    column_names = ['Cylinders','Displacement','Horsepower','Weight', 'Acceleration', 'Model Year', 'USA', 'Europe', 'Japan']

    def __init__(self, model_path):
        self.model = keras.models.load_model(model_path)

    @classmethod
    def estimate(self, payload):
        raw_data = payload["data"]
        items = pd.DataFrame([raw_data], columns=self.column_names)
        prediction = self.model.predict(items).flatten()[0]
        return 'The predicted value is: ' + str(prediction) + ' MPG'
