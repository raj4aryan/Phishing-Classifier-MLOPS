import os, sys
import yaml
import dill

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