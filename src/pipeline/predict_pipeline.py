import os
import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model_trainer.pkl")
            preprocessor_path=os.path.join('artifacts','proprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(  self,
        cylinders: int,
        displacement: float,
        horsepower: int,
        weight: float,
        acceleration: float):

        self.cylinders = cylinders

        self.displacement = displacement

        self.horsepower = horsepower

        self.weight = weight

        self.acceleration = acceleration

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "cylinders": [self.cylinders],
                "displacement": [self.displacement],
                "horsepower": [self.horsepower],
                "weight": [self.weight],
                "acceleration": [self.acceleration],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)