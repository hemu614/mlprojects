from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.componetns.data_ingestion import DataIngestion, DataIngestionConfig
import sys


if __name__ == "__main__":
    logging.info("Starting the application")

    try:
        #data_ingestion = DataIngestionConfig()
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
        logging.info("Data ingestion completed")

    except Exception as e:
        logging.info("An error occurred")
        raise CustomException(e, sys) 