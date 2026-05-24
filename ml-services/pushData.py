import os, sys
from dotenv import load_dotenv
load_dotenv()

MONGODB_URI = os.getenv("MONGO_URI")

import certifi
ca = certifi.where()

import pandas as pd
import numpy as np
import pymongo
import json
from networkSecurity.exceptions.exceptions import CustomException
from networkSecurity.logging.logger import logging

class NetworkDataExtract:
    def __int__(self):
        pass

    def csv_to_json_converter(self, filePath):
        try:
            data = pd.read_csv(filePath)
            data.reset_index(drop=True, inplace= True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise CustomException(e, sys)
        
    def insert_data_mongodb(self, database, collection, records):
        try:
            self.database = database
            self.collection = collection
            self.records = records
            self.mongoClient = pymongo.MongoClient(MONGODB_URI)
            self.database = self.mongoClient[self.database]
            self.collection = self.database[self.collection]

            self.collection.insert_many(self.records)
            return len(self.records)
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    try:
        FILE_PATH = os.path.join("Network_Data","phisingData.csv")
        DATABASE = "MLDB"
        COLLECTION = "NetworkData"
        
        ndeObj = NetworkDataExtract()
        records = ndeObj.csv_to_json_converter(filePath=FILE_PATH)
        res = ndeObj.insert_data_mongodb(records= records, collection= COLLECTION, database= DATABASE)
        print(res)

    except Exception as e:
        raise CustomException(e, sys)
