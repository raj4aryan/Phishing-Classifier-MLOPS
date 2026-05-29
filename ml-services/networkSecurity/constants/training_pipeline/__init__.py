import os, sys
import numpy as np

TARGET_COLUMN = "Result"
PIPELINE_NAME: str = "networkSecurity"
ARTIFACT_DIR: str = "artifacts"
FILE_NAME: str = "PhishingData.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"
PREPROCESSING_OBJECT_FILE_NAME: str = "preprocessor.pkl"

SCHEMA_FILE_PATH = os.path.join("data_schema", "schema.yaml")

SAVED_MODEL_DIR:str = "saved_models"
MODEL_FILE_NAME: str = "model.pkl"

# Data Ingestion
DATA_INGESTION_COLLECTION_NAME: str = "NetworkData"
DATA_INGESTION_DATABASE_NAME: str = "MLDB"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str ="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2

# Data Validation
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATAION_VALID_DIR: str ="validated"
DATA_VALIDATAION_INVALID_DIR: str ="invalid"
DATA_VALIDATAION_DRIFT_REPORT_DIR: str ="drift_report"
DATA_VALIDATAION_DRIFT_REPORT_FILE_NAME: str ="report.yaml"

# Data Transformation
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA: str = "transformed"
PREPROCESSING_OBJECT_FILE_PATH: str = "preprocessor_model"

# using KNN imputer
DATA_TRANSFORMATION_IMPUTE_PARAMS: dict = {
    "missing_values": np.nan,
    "n_neighbors": 3,
    "weights": "uniform"
}

# Model Training
MODEL_TRAINER_PATH: str = "trained_model"
MODEL_TRAINER_FILE_NAME: str = "networkSecurityModel.pkl"
MODEL_TRAINER_EXPECTED_ACCURACY: float = 0.86
MODEL_TRAINER_OVERFITTING_UNDERFITTING_THRESHOLD: float = 0.05

