import os, sys
import yaml
import dill
import numpy as np
import pickle

from networkSecurity.exceptions.exceptions import CustomException
from networkSecurity.logging.logger import logging

from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score

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
    
def load_numpy_array(filePath: str) -> np.array:
    try:
        logging.info("Loading numpy array")
        with open(filePath, "rb") as file:
            array = np.load(file)
        return array
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
    
def load_object(filePath: str) -> object:
    try:
        logging.info("Loading Object")
        with open(filePath, "rb") as file:
            model = pickle.load(file)
        return model
    except Exception as e:
        raise CustomException(e, sys)
    

def evaluate_models(X_train, y_train, X_test, y_test, models:dict, param_grids:dict):
    try:
        model_report = {}
        for modelName, model in models.items():
            params = param_grids[modelName]
            grid = GridSearchCV(estimator=model, param_grid=params, cv=3, n_jobs=-1)
            grid.fit(X_train, y_train)
 
            model.set_params(**grid.best_params_)
            model.fit(X_train, y_train)

            y_pred = model.predict(X_test)
            test_model_score = r2_score(y_test, y_pred)

            model_report[modelName] = test_model_score

            return model_report

    except Exception as e:
        raise CustomException(e, sys)