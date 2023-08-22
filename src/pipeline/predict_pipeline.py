# Import necessary libraries
import os
import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

# Define a class for the prediction pipeline
class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            # Define paths to the saved model and preprocessor artifacts
            model_path=os.path.join("artifacts","model_trainer.pkl")
            preprocessor_path=os.path.join('artifacts','proprocessor.pkl')
             # Print a message before loading artifacts
            print("Before Loading")
            
            # Load the trained model and preprocessor using custom utility function
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            
            # Print a message after loading artifacts
            print("After Loading")
            
            # Transform input features using the preprocessor
            data_scaled=preprocessor.transform(features)
            
            # Make predictions using the loaded model
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            # If any exception occurs, raise a custom exception with the original exception and system info
            raise CustomException(e,sys)


# Define a class for custom data input
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
            # Create a dictionary with the custom data input
            custom_data_input_dict = {
                "cylinders": [self.cylinders],
                "displacement": [self.displacement],
                "horsepower": [self.horsepower],
                "weight": [self.weight],
                "acceleration": [self.acceleration],
            }
            
            # Convert the dictionary to a pandas DataFrame
            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            # If any exception occurs, raise a custom exception with the original exception and system info
            raise CustomException(e, sys)