from networkSecurity.exceptions.exceptions import CustomException
from networkSecurity.logging.logger import logging
from networkSecurity.components.data_ingestion import DataIngestion
from networkSecurity.entity.config_entity import DataIngestionConfig
from networkSecurity.entity.config_entity import TrainingPipelineConfig
import sys

if __name__ == "__main__":
    try:
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        dataingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        print(dataingestion.initiate_data_ingestion())

    except Exception as e:
        raise CustomException(e, sys)