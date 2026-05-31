import os, sys
from networkSecurity.logging.logger import logging
from networkSecurity.exceptions.exceptions import CustomException
from networkSecurity.entity.config_entity import ModelTrainerConfig
from networkSecurity.entity.artifact_entity import DataTransformationArtifact, ModelTrainerArtifact

from networkSecurity.utils.main_utils.utils import save_object, load_object
from networkSecurity.utils.main_utils.utils import load_numpy_array, evaluate_models
from networkSecurity.utils.ml_utils.metric.classification_metric import get_classification_score
from networkSecurity.utils.ml_utils.model.estimator import NetworkModel



from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV

import mlflow
import dagshub
dagshub.init(repo_owner='raj8aryan4tuity', repo_name='Phishing-Classifier-MLOPS', mlflow=True)


class ModelTrainer:
    def __init__(self, data_transformation_artifact: DataTransformationArtifact, model_trainer_config: ModelTrainerConfig):
        try:
            self.data_transformation_artifact = data_transformation_artifact
            self.model_trainer_config = model_trainer_config
        except Exception as e:
            raise CustomException(e, sys)
        
    def track_mlflow(self, best_model, classificationMetric):
        with mlflow.start_run():
            f1_score = classificationMetric.f1_score
            precision_score = classificationMetric.precision_score
            recall_score = classificationMetric.recall_score

            mlflow.log_metric("f1_score",f1_score)
            mlflow.log_metric("precision_score",precision_score)
            mlflow.log_metric("recall_score",recall_score)

            mlflow.sklearn.log_model(best_model, name="model")

        
    def train_model(self, X_train, y_train, X_test, y_test):
        models = {
            "LogisticRegression": LogisticRegression(),
            "KNeighborsClassifier": KNeighborsClassifier(),
            "SVC": SVC(),
            "DecisionTreeClassifier": DecisionTreeClassifier(),
            "AdaBoostClassifier": AdaBoostClassifier(),
            "GradientBoostingClassifier": GradientBoostingClassifier(),
            "RandomForest": RandomForestClassifier(verbose=1)
        }
        param_grids = {
            "LogisticRegression": {
                "C": [0.001, 0.01, 0.1, 1, 10, 100]
            },
            "KNeighborsClassifier": {
                "n_neighbors": [3, 5, 7, 9, 11],
                "metric": ["euclidean", "manhattan", "minkowski"]
            },
            "SVC": {
                "C": [0.1, 1, 10, 100],
                "kernel": ["linear", "rbf"],
                "gamma": ["scale", "auto", 0.1, 0.01, 0.001],
                "degree": [2, 3, 4]
            },
            "DecisionTreeClassifier": {
                "criterion": ["gini", "entropy", "log_loss"],
                "splitter": ["best", "random"],
                "max_depth": [None, 5, 10, 20, 30],
            },
            "AdaBoostClassifier": {
                "n_estimators": [50, 100, 200],
                "learning_rate": [0.001, 0.01, 0.1, 1]
            },
            "GradientBoostingClassifier": {
                "loss": ["log_loss", "exponential"],
                "learning_rate": [0.01, 0.1, 0.2],
                "n_estimators": [100, 200, 300],
                "max_depth": [3, 5, 7]
            },
            "RandomForest": {
                "n_estimators": [100, 200, 300],
                "criterion": ["gini", "entropy", "log_loss"],
                "max_depth": [None, 10, 20, 30],
                "bootstrap": [True, False]
            }
        }

        model_report:dict = evaluate_models(X_train=X_train, y_train= y_train, X_test=X_test, y_test= y_test, models=models, param_grids=param_grids)

        best_model_score = max(sorted(model_report.values()))

        best_model_name = list(model_report.keys())[
            list(model_report.values()).index(best_model_score)
        ]

        best_model = models[best_model_name]

        y_train_pred = best_model.predict(X_train)
        classification_train_metric = get_classification_score(y_train, y_train_pred)

        y_test_pred = best_model.predict(X_test)
        classification_test_metric = get_classification_score(y_test, y_test_pred)

        preprocessor = load_object(self.data_transformation_artifact.preprocessor_object_file_path)

        model_dir_path = os.path.dirname(self.model_trainer_config.trained_model_file_path)
        os.makedirs(model_dir_path, exist_ok=True)

        Network_Model = NetworkModel(preprocessor = preprocessor, model = best_model)
        save_object(self.model_trainer_config.trained_model_file_path, object=Network_Model)

        print("best_model_name: ", best_model_name)

        #creating artifacts
        model_tainer_artifact = ModelTrainerArtifact(
            trained_model_file_path=self.model_trainer_config.trained_model_file_path,
            train_metric_artifact=classification_train_metric,
            test_metric_artifact=classification_test_metric
        )

        #saving the final_models / model pusher
        save_object("models/model.pkl", best_model)
        save_object("models/preprocessor.pkl", preprocessor)

        ## Track the experiments with mlflow
        # train
        self.track_mlflow(best_model=best_model, classificationMetric=classification_train_metric)

        # test
        self.track_mlflow(best_model=best_model, classificationMetric=classification_test_metric)

        logging.info(f"Best Model: {best_model_name}\nTrain Classification Report:\n{classification_train_metric}")
        logging.info(f"Best Model: {best_model_name}\nTest Classification Report:\n{classification_test_metric}")

        return model_tainer_artifact



        
    def initiate_model_training(self)->ModelTrainerArtifact:
        try:
            trained_file_path = self.data_transformation_artifact.transformed_train_data_file_path
            test_file_path = self.data_transformation_artifact.transformed_test_data_file_path

            #loading trained and test data
            train_arr = load_numpy_array(trained_file_path)
            test_arr = load_numpy_array(test_file_path)

            X_train, y_train, X_test, y_test = (
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]
            )

            model_trainer_artifact = self.train_model(X_train, y_train, X_test, y_test)

            return model_trainer_artifact

        except Exception as e:
            raise CustomException(e, sys)

