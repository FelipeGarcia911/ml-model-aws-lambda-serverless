from tensorflow import keras
import pandas as pd
from PIL import Image
import numpy as np

model_path = "./src/app/routes/image_labeling/model.keras"
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

class ImageLabeling:
    model = keras.models.load_model(model_path)

    def __init__(self, model_path):
        self.model = keras.models.load_model(model_path)


    def getPredictedClass(prediction):
        return class_names[np.argmax(prediction)]
    
    def getPredictedProbability(prediction):
        return round(np.max(prediction)*100, 2)
    
    def getImageArray(image_file):
        image = Image.open(image_file)
        image_array = (np.expand_dims(np.array(image)/255,0))   

        return image_array

    @classmethod
    def estimate(self, image_file):
        image_array = self.getImageArray(image_file) 
        predictions_single = self.model.predict(image_array)
        
        label = self.getPredictedClass(predictions_single[0])
        probability = self.getPredictedProbability(predictions_single[0])

        message = "The predicted class is: " + label + " with a probability of: " + str(probability) + "%"
        
        result = { "message": message, "label": label, "probability": str(probability) }

        return result

