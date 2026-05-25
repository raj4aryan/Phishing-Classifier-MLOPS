from networkSecurity.exceptions.exceptions import CustomException
from networkSecurity.logging.logger import logging
from networkSecurity.components.data_ingestion import DataIngestion
from networkSecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig
from networkSecurity.entity.config_entity import TrainingPipelineConfig
import sys

from networkSecurity.components.data_validation import DataValidation

if __name__ == "__main__":
    try:
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        dataingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        data_ingestion_artifact = dataingestion.initiate_data_ingestion()
        print(data_ingestion_artifact)
        logging.info("Data Ingestion Completed")

        data_validation_config = DataValidationConfig(training_pipeline_config=training_pipeline_config)
        data_validation = DataValidation(data_ingestion_artifact, data_validation_config)
        print(data_validation.initiate_data_validation())
        logging.info("Data Validation Completed")

    except Exception as e:
        raise CustomException(e, sys)