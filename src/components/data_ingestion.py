# The main aim is to read the dataset from some specific data source ( which can be from big data team or cloud team or live stream data)
#Our aim is to read the data and split it into training and test data

import os
import sys

from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses  import dataclass


#why data ingestion config called : these are the input whic we give to data ingestion component and now data igestion component shows where to train path and filepath
@dataclass                               #
class DataIngestionConfig:
    train_data_path: str = os.path.join('atrifacts', "train_data") # data ingestion will save train.csv in this particular path
    test_data_path: str = os.path.join('atrifacts', "test_data")
    raw_data_path: str = os.path.join('atrifacts', "raw_data")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def intiate_data_ingestion(self):
        logging.info("entered the data ingestion method") #readig the dataset in very easy way
        try:                                               # if error will come then to read the error
            df=pd.read_csv("/Users/00_Projects/00_mlproject/notebook/data/data/StudentsPerformance.csv")        # Read the dataset , here from C drive, but it cannbe from UI
            logging.info("Read the datset as dataframe")  #always loggin the data


            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)                              # convert dataset to CSV

            logging.info("Train test spilt initiated") #
            train_set, test_set =train_test_split(df, test_size=0.2, random_state=42)                             # save data in the specific path        

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of data is completed")

            return(
                self.ingestion_config.train_data_path, # this infor is required for data transformation. the data transformation will grab this two points and process it 
                self.ingestion_config.test_data_path
            )


        except Exception as e:
            raise CustomException(e, sys)
        
if __name__ == "__main__":
    obj=DataIngestion()
    obj.intiate_data_ingestion()