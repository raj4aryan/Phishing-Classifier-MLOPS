import sys, os
import certifi
ca = certifi.where()

from dotenv import load_dotenv
load_dotenv()

mongodb_uri = os.getenv("MONGO_URI")

import pymongo
from networkSecurity.pipeline.training_pipeline import TrainingPipeline
from networkSecurity.logging.logger import logging
from networkSecurity.exceptions.exceptions import CustomException
from networkSecurity.constants.training_pipeline import DATA_INGESTION_COLLECTION_NAME, DATA_INGESTION_DATABASE_NAME
from networkSecurity.utils.main_utils.utils import load_object
from networkSecurity.utils.ml_utils.model.estimator import NetworkModel

from fastapi import FastAPI, File, UploadFile, Request
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run as app_run
from fastapi.responses import Response
from starlette.responses import RedirectResponse
import pandas as pd
app = FastAPI()
origins = ["*"]

client = pymongo.MongoClient(mongodb_uri, tlsCAFile = ca)
database = client[DATA_INGESTION_DATABASE_NAME]
collection = database[DATA_INGESTION_COLLECTION_NAME]

preprocessor = load_object("models/preprocessor.pkl")
model = load_object("models/model.pkl")

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def train_route():
    try:
        train_pipeline = TrainingPipeline()
        train_pipeline.run_pipeline()

        return Response("Training is successful", status_code=200)
    except Exception as e:
        raise CustomException(e, sys)
    
@app.post("/predict")
async def predict_route(request:Request, file:UploadFile=File(...)):
    try:
        df = pd.read_csv(file.file)
        networkModel = NetworkModel(preprocessor=preprocessor, model= model)
        y_pred, confidence_score = networkModel.predict(df)
        df["predicted_output"] = y_pred
        df["confidence_score"] = confidence_score
        df["prediction_label"] = df["predicted_output"].map({
            0: "Phishing",
            1: "Legitimate"
        })
        

        return {"prediction": df.to_dict(orient="records")}
    
    
    except Exception as e:
        raise CustomException(e, sys)
    




if __name__ == "__main__":
    app_run(app, host = "0.0.0.0", port=8000)