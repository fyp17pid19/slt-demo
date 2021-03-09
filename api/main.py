from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI,File,UploadFile

from fastapi.encoders import jsonable_encoder

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


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post('/veng')
def read_video():
    return {"object": "hello"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post("/video/data")
async def video_from_fronend(file:UploadFile=File(...)):
    # text = base64.b64encode(file.file.read())
    # file = open("textTest.txt", "wb") 
    # file.write(text)
    # file.close()
    fh = open("video.mp4", "wb")
    fh.write(file.file.read())
    fh.close()
    # fh=open("video.mp4", mode="rb")
    # return {"Hello":"Video"}
    file_path="video.mp4"
    return {"Video File":"Created"}
