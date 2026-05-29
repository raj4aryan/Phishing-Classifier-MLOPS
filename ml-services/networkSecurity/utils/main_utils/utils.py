import os, sys
import yaml
import dill
import numpy as np
import pickle

from networkSecurity.exceptions.exceptions import CustomException
from networkSecurity.logging.logger import logging

def read_yaml_file(filePath: str) -> dict:
    try:
        with open(filePath, "rb") as file:
            return yaml.safe_load(file)
        
    except Exception as e:
        raise CustomException(e, sys)
    

def write_yaml_file(filePath: str, content: object, replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exists(filePath):
                os.remove(filePath)
        os.makedirs(os.path.dirname(filePath), exist_ok=True)
        with open(filePath, "w") as file:
            yaml.dump(content, file)
        
    except Exception as e:
        raise CustomException(e, sys)
    

def save_numpy_array(filePath: str, array: np.array) -> None:
    try:
        logging.info("Saving numpy array")
        os.makedirs(os.path.dirname(filePath), exist_ok=True)
        with open(filePath, "wb") as file:
            np.save(file, array)
        
    except Exception as e:
        raise CustomException(e, sys)
        

def save_object(filePath: str, object: object) -> None:
    try:
        logging.info("Saving Object")
        os.makedirs(os.path.dirname(filePath), exist_ok=True)
        with open(filePath, "wb") as file:
            pickle.dump(object, file)
        
    except Exception as e:
        raise CustomException(e, sys)