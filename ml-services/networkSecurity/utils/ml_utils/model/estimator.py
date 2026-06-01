import sys
from networkSecurity.logging.logger import logging
from networkSecurity.exceptions.exceptions import CustomException
from networkSecurity.constants.training_pipeline import SAVED_MODEL_DIR, MODEL_FILE_NAME

class NetworkModel:
    def __init__(self, preprocessor, model):
        try:
            self.preprocessor = preprocessor
            self.model = model
        except Exception as e:
            raise CustomException(e, sys)
        
    def predict(self, x):
        try: 
            x_transform = self.preprocessor.transform(x)
            y_hat = self.model.predict(x_transform)
            probabilities = self.model.predict_proba(x_transform)
            confidence_scores = probabilities.max(axis=1)
            return y_hat, confidence_scores
        
        except Exception as e:
            raise CustomException(e, sys)
        
# class NetworkModel:
#     def __init__(self, preprocessor, model):
#         try:
#             self.preprocessor = preprocessor
#             self.model = model

#         except Exception as e:
#             raise CustomException(e, sys)

#     def predict(self, x):
#         try:
#             x_transform = self.preprocessor.transform(x)

#             y_hat = self.model.predict(x_transform)

#             probabilities = self.model.predict_proba(x_transform)

#             confidence_scores = []

#             for pred, prob in zip(y_hat, probabilities):
#                 confidence_scores.append(float(prob[pred]))

#             return y_hat, confidence_scores

#         except Exception as e:
#             raise CustomException(e, sys)