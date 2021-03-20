from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile

from fastapi.encoders import jsonable_encoder
from frames import Frames
import time

app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}


@app.post("/process/eng")
async def process_eng(file: UploadFile = File(...)):
    fh = open("video.mp4", "wb")
    fh.write(file.file.read())
    fh.close()
    file_path = "video.mp4"
    time.sleep(2)
    return {
        "Number of Signs": 5,
        "Sign 1": "A",
        "Sign 2": "B",
        "Sign 3": "C",
        "Sign 4": "D",
        "Sign 5": "E",
    }


@app.post("/process/urdu")
async def process_urdu(file: UploadFile = File(...)):
    fh = open("video.mp4", "wb")
    fh.write(file.file.read())
    fh.close()
    file_path = "video.mp4"
    return {"Video File": file.filename}
