from fastapi import FastAPI
from relic_processing import processRelicFromJson
app = FastAPI()

file_path = "../tests/march7th.min.json"
@app.get("/processrelicdata")
async def processrelicdata():
    return processRelicFromJson()
