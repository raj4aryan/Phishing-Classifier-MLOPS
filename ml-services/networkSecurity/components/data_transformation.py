import sys, os
from networkSecurity.logging.logger import logging
from networkSecurity.exceptions.exceptions import CustomException
from networkSecurity.entity.config_entity import DataTransformationConfig
from networkSecurity.entity.artifact_entity import (DataTransformationArtifact, DataValidationArtifact)
from networkSecurity.constants.training_pipeline import (DATA_TRANSFORMATION_IMPUTE_PARAMS, TARGET_COLUMN)
from networkSecurity.utils.main_utils.utils import save_numpy_array, save_object

import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline

class DataTransformation:
    def __init__(self, data_validation_artifact:DataValidationArtifact, data_transformation_config: DataTransformationConfig):
        try:
            self.data_validation_artifact = data_validation_artifact
            self.data_transformation_config = data_transformation_config
        except Exception as e:
            raise CustomException(e, sys)
    
    @staticmethod
    def read_data(filePath):
        try:
            return pd.read_csv(filePath)
        
        except Exception as e:
            raise CustomException(e, sys)
        
    def get_data_transformation_object(cls)->Pipeline:
        logging.info("Entering get_data_transformation_object method of Transformation Class")
        try:
            imputer = KNNImputer(**DATA_TRANSFORMATION_IMPUTE_PARAMS)
            logging.info(f"Initialise KNN IMPUTER - {DATA_TRANSFORMATION_IMPUTE_PARAMS}")

            processor: Pipeline = Pipeline([("imputer", imputer)])

            return processor

        
        except Exception as e:
            raise CustomException(e, sys)
        
    

    def initiate_data_transformation(self)->DataTransformationArtifact:
        logging.info("Initiating Data Transformation")
        try:
            traindf = self.read_data(self.data_validation_artifact.valid_train_file_path)
            testdf = self.read_data(self.data_validation_artifact.valid_test_file_path)

            # training dataframe
            input_feature_train_df = traindf.drop(columns=[TARGET_COLUMN])
            target_feature_train_df = traindf[TARGET_COLUMN]
            target_feature_train_df = target_feature_train_df.replace(-1, 0)

            # test dataframe
            input_feature_test_df = testdf.drop(columns=[TARGET_COLUMN])
            target_feature_test_df = testdf[TARGET_COLUMN]
            target_feature_test_df = target_feature_test_df.replace(-1, 0)

            preprocessor: Pipeline = self.get_data_transformation_object()
            preprocessor_object = preprocessor.fit(input_feature_train_df)
            transformed_trained_input_feature = preprocessor.transform(input_feature_train_df)
            transformed_test_input_feature = preprocessor.transform(input_feature_test_df)

            train_arr = np.c_[transformed_trained_input_feature, np.array(target_feature_train_df)]
            test_arr = np.c_[transformed_test_input_feature, np.array(target_feature_test_df)]

            save_numpy_array(self.data_transformation_config.transformed_trained_file_path, train_arr)
            save_numpy_array(self.data_transformation_config.transformed_test_file_path, test_arr)
            save_object(self.data_transformation_config.preprocessor_object_file_path, preprocessor_object)

            #preparing artifacts
            data_transformation_artifact = DataTransformationArtifact(
                transformed_train_data_file_path = self.data_transformation_config.transformed_trained_file_path,transformed_test_data_file_path = self.data_transformation_config.transformed_test_file_path,
                preprocessor_object_file_path = self.data_transformation_config.preprocessor_object_file_path
            )

            return data_transformation_artifact


        except Exception as e:
            raise CustomException(e, sys)