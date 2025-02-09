import sys,os
from wasteDetection.logger import logging
from wasteDetection.exception import AppException
from wasteDetection.components.data_ingestion import DataIngestion
from wasteDetection.components.data_validation import DataValidation

from wasteDetection.entity.config_entity import (DataIngestionConfig,DataValidationConfig)

from wasteDetection.entity.artifacts_entity import (DataIngestionArtifact,DataValidationArtifact)


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()
        
    def start_data_ingestion(self)-> DataIngestionArtifact:
        try:
            logging.info(
                "Entered the start _data_ingestion methodf of TrainPipelie class"
            ) 
            logging.info("Getting the data from url")
            
            data_ingestion = DataIngestion(
                data_ingestion_config = self.data_ingestion_config
                
            )
            
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("got the data from url")
            logging.info("Exited the start_data_ingestion method of TrainPipeline class")
            
            return data_ingestion_artifact
        except AppException as e:
            raise AppException(e,sys)
    def run_pipeline(self) -> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
        except Exception as e:
            raise AppException(e,sys)