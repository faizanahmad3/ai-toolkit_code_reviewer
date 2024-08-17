from fastapi import APIRouter, Depends
import os
from src.core.auth import get_api_key

from typing import Dict
from src.utils.logger import setup_logger
from src.utils.utilities import (
    create_directories,
    extract_zip
)

from fastapi import File, HTTPException, UploadFile
from src.config import settings as e_var
import logging

info_logger = setup_logger(__name__, level=logging.INFO)
debug_logger = setup_logger(__name__, level=logging.DEBUG)
error_logger = setup_logger(__name__, level=logging.ERROR)
warning_logger = setup_logger(__name__, level=logging.WARNING)

upload_router = APIRouter()


@upload_router.post("/upload_zip-file/", dependencies=[Depends(get_api_key)])
async def handle_file_upload(file: UploadFile = File(...)) -> Dict:
    if not file.filename.endswith(".zip"):
        warning_logger.warning("Attempted to upload a non-zip file.")
        raise HTTPException(
            status_code=400, detail="Invalid file format. Only .zip files are allowed."
        )

    create_directories()

    try:
        file_path = os.path.join(e_var.UPLOAD_FOLDER, file.filename)
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())
        info_logger.info(f"File '{file.filename}' uploaded successfully to '{file_path}'.")
    except Exception as e:
        error_logger.error(f"File upload failed: {e}")
        raise HTTPException(status_code=500, detail="File upload failed.")

    try:
        extracted_zip_path = extract_zip(file_path)
        info_logger.info(
            f"File '{file.filename}' extracted successfully to '{extracted_zip_path}'."
        )
    except Exception as e:
        error_logger.error(f"Error extracting file '{file.filename}': {e}")
        raise HTTPException(status_code=500, detail="Error extracting file.")

    return {"files_path": extracted_zip_path}
