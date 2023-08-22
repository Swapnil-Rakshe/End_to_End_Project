# Import necessary libraries and modules
import os
import sys
from src.exception import CustomException  # Import CustomException from src.exception module
from src.logger import logging  # Import logging from src.logger module
import pandas as pd  # Import pandas library

from sklearn.model_selection import train_test_split  # Import train_test_split from sklearn.model_selection
from dataclasses import dataclass  # Import dataclass decorator

from src.components.data_transformation import DataTransformation  # Import DataTransformation class
from src.components.data_transformation import DataTransformationConfig  # Import DataTransformationConfig class

from src.components.model_trainer import ModelTrainerConfig  # Import ModelTrainerConfig class
from src.components.model_trainer import ModelTrainer  # Import ModelTrainer class

# Define a dataclass for DataIngestionConfig with default paths
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")

# Define the DataIngestion class
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()  # Initialize with DataIngestionConfig defaults

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv('notebook\data\mpg.csv')  # Read CSV file into a DataFrame
            logging.info('Read the dataset as dataframe')

            # Create necessary directories if they don't exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Save the raw data to a file
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train test split initiated")
            # Perform train-test split
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save train and test sets to separate files
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)  # Raise a CustomException with the caught exception

if __name__ == "__main__":
    obj = DataIngestion()  # Create an instance of DataIngestion
    train_data, test_data = obj.initiate_data_ingestion()  # Perform data ingestion

    data_transformation = DataTransformation()  # Create an instance of DataTransformation
    # Perform data transformation on train and test data
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)

    model_trainer = ModelTrainer()  # Create an instance of ModelTrainer
    # Initiate model training and print the result
    print(model_trainer.initiate_model_trainer(train_arr, test_arr))
