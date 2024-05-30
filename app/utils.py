import os
from cryptography.fernet import Fernet
from fastapi import UploadFile

# Generate a key and instantiate a Fernet instance
key = Fernet.generate_key()
cipher_suite = Fernet(key)

UPLOAD_DIR = "uploads/"
VIDEO_DIR = "data/videos/video.mp4"

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

if not os.path.exists(VIDEO_DIR):
    os.makedirs(VIDEO_DIR)

async def save_encrypted_file(file: UploadFile) -> str:
    contents = await file.read()
    encrypted_data = cipher_suite.encrypt(contents)
    
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(encrypted_data)
    
    return file_path

def get_encrypted_file_path(file_name: str) -> str:
    file_path = os.path.join(UPLOAD_DIR, file_name)
    return file_path

async def save_video_file(file: UploadFile) -> str:
    contents = await file.read()
    
    file_path = os.path.join(VIDEO_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(contents)
    
    return file_path

def get_video_file_path(file_name: str) -> str:
    file_path = os.path.join(VIDEO_DIR, file_name)
    return file_path
