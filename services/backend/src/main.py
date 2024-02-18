from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from relic_processing import processRelicFromJson
app = FastAPI()

origins = [
    "http://localhost:5174"  # 这里是你前端的地址
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/processrelicdata")
async def processrelicdata(request: Request):
    json_data = await request.json()
    return processRelicFromJson(json_data)
