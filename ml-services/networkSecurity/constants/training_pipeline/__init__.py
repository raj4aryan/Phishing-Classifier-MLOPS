import os, sys

TARGET_COLUMN = "Result"
PIPELINE_NAME: str = "networkSecurity"
ARTIFACT_DIR: str = "artifacts"
FILE_NAME: str = "PhishingData.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

SCHEMA_FILE_PATH = os.path.join("data_schema", "schema.yaml")

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
