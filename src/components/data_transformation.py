# Import necessary libraries and modules
import os
import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from src.exception import CustomException  # Import CustomException from src.exception module
from src.logger import logging  # Import logging from src.logger module
from sklearn.pipeline import Pipeline  # Import Pipeline from sklearn.pipeline
from sklearn.impute import SimpleImputer  # Import SimpleImputer from sklearn.impute
from sklearn.preprocessing import StandardScaler  # Import StandardScaler from sklearn.preprocessing
from sklearn.compose import ColumnTransformer  # Import ColumnTransformer from sklearn.compose
from src.utils import save_object  # Import save_object function from src.utils module

# Define a dataclass for DataTransformationConfig with default paths
@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path: str = os.path.join('artifacts', "proprocessor.pkl")

# Define the DataTransformation class
class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()  # Initialize with DataTransformationConfig defaults
    
    def get_data_transformer_object(self):
        '''
        Function to get the data transformation object
        '''
        try:
            numerical_columns = ['horsepower']
            transformation_columns = ['cylinders', 'displacement', 'weight', 'acceleration']
            
            # Create a pipeline for transforming numerical columns
            trans_pipeline = Pipeline(
                steps=[
                    ("scaler", StandardScaler())
                ]
            )
            
            # Create a pipeline for imputing and scaling numerical columns
            num_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(missing_values='?', strategy='most_frequent')),
                    ("scaler", StandardScaler())
                ]
            )
            
            logging.info("Transformation pipeline executed successfully")
            logging.info("Numerical pipeline executed successfully")
            
            # Create a ColumnTransformer to apply different pipelines to different columns
            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline, numerical_columns),
                    ("trans_pipeline", trans_pipeline, transformation_columns)
                ]
            )
            
            return preprocessor
        
        except Exception as e:
            raise CustomException(e, sys)
        
    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)  # Read the training data CSV file
            test_df = pd.read_csv(test_path)  # Read the testing data CSV file
            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")
            preprocessing_obj = self.get_data_transformer_object()  # Get the preprocessing object
            
            target_column_name = "mpg"
            numerical_columns = ['horsepower']
            drop_columns = ['mpg', 'model year', 'origin', 'car name']
            
            # Separate input features and target features for training data
            input_feature_train_df = train_df.drop(columns=drop_columns, axis=1)
            target_feature_train_df = train_df[target_column_name]
            
            # Separate input features and target features for testing data
            input_feature_test_df = test_df.drop(columns=drop_columns, axis=1)
            target_feature_test_df = test_df[target_column_name]
            
            logging.info("Applying preprocessing object on training dataframe and testing dataframe.")
            # Transform input features using the preprocessing object
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)
            
            # Combine input features and target features into arrays
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info("Saved preprocessing object.")
            # Save the preprocessing object using the save_object function
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
             
        except Exception as e:
            raise CustomException(e, sys)
