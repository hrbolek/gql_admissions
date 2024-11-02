import os
from uoishelpers.feeders import ImportModels
from uoishelpers.dataloaders import readJsonFile

from src.DBDefinitions import (
    AdmissionModel
)

def get_demodata(filename="./systemdata.json"):
    return readJsonFile(filename)

async def initDB(asyncSessionMaker, filename="./systemdata.json"):

    DEMODATA = os.environ.get("DEMODATA", None) in ["True", "true"]    
    if DEMODATA:
        dbModels = [
            AdmissionModel
            ]
    else:
        dbModels = []

    jsonData = get_demodata(filename=filename)
    await ImportModels(asyncSessionMaker, dbModels, jsonData)
    pass