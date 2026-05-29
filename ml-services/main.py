from networkSecurity.exceptions.exceptions import CustomException
from networkSecurity.logging.logger import logging
from networkSecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig
from networkSecurity.entity.config_entity import TrainingPipelineConfig
import sys

from networkSecurity.components.data_ingestion import DataIngestion
from networkSecurity.components.data_validation import DataValidation
from networkSecurity.components.data_transformation import DataTransformation

if __name__ == "__main__":
    try:
        training_pipeline_config = TrainingPipelineConfig()

        #Data Ingestion
        data_ingestion_config = DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        dataingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        data_ingestion_artifact = dataingestion.initiate_data_ingestion()
        print("Data Ingestion o/p: ",data_ingestion_artifact)
        logging.info("Data Ingestion Completed")

        #Data Validation
        data_validation_config = DataValidationConfig(training_pipeline_config=training_pipeline_config)
        data_validation = DataValidation(data_ingestion_artifact, data_validation_config)
        data_validation_artifact = data_validation.initiate_data_validation()
        print("\nData Validation o/p: ",data_validation_artifact)
        logging.info("Data Validation Completed")

        #Data Transformation
        data_transformation_config = DataTransformationConfig(training_pipeline_config)
        data_transformation = DataTransformation(data_validation_artifact=data_validation_artifact, data_transformation_config=data_transformation_config)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        print("\nData Tranfomation o/p: ",data_transformation_artifact)
        logging.info("Data Transformation Completed")

    except Exception as e:
        raise CustomException(e, sys)