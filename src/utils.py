import os
import numpy as np
import pandas as pd
import sys
import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV


from src.exception import CustomException

# Function to save an object to a file using pickle
def save_object(file_path, obj):
    # Create the directory path if it doesn't exist
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)
        
        # Serialize and save the object to the specified file
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
            
    # Raise a custom exception with error details if any exception occurs
    except Exception as e:
        raise CustomException(e, sys)

# Function to evaluate multiple models on training and test data
def evaluate_models(X_train, y_train,X_test,y_test,models,param):
    try:
        report = {}
        # Iterate over the models and their corresponding hyperparameters
        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]

            # Perform grid search for hyperparameter tuning
            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            # Set the best hyperparameters to the model
            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train) # Train the model

            #model.fit(X_train, y_train)  # Train model
            # Make predictions on training and test data
            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)
            
            # Calculate R-squared scores for training and test data
            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            # Store the test R-squared score in the report
            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        # Raise a custom exception with error details
        raise CustomException(e, sys)

# Function to load an object from a file using pickle
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        # Raise a custom exception with error details
        raise CustomException(e, sys)