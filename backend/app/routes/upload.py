from fastapi import APIRouter
from app.models.upload_request import UploadRequest

router = APIRouter()

@router.post("/api/upload/presigned-url")
def generate_presigned_url(data: UploadRequest):

    allowed_extensions = [".docx", ".pptx"]

    if not data.fileName.lower().endswith(tuple(allowed_extensions)):
        return {
            "error": "Tipo de archivo no permitido"
        }

    return {
        "message": "archivo válido"
    }