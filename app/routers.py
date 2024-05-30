from fastapi import APIRouter, UploadFile, File
from app.utils import save_encrypted_file, get_encrypted_file_path, save_video_file, get_video_file_path

router = APIRouter()

@router.post("/video.mp4/")
async def upload_file(file: UploadFile = File(...)):
    file_location = await save_encrypted_file(file)
    return {"file_location": file_location}

@router.post("/video.mp4/")
async def upload_video(file: UploadFile = File(...)):
    file_location = await save_video_file(file)
    return {"file_location": file_location}

@router.get("/files/{file_name}")
async def get_file(file_name: str):
    file_path = get_encrypted_file_path(file_name)
    return {"file_path": file_path}

@router.get("/videos/{file_name}")
async def get_video(file_name: str):
    file_path = get_video_file_path(file_name)
    return {"file_path": file_path}
