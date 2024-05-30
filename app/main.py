from fastapi import FastAPI, UploadFile, File
from app.routers import router

app = FastAPI()

app.include_router(router)
