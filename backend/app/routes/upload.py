from fastapi import APIRouter, HTTPException
from app.models.upload_request import UploadRequest
from app.services.s3_service import S3Service

s3_service = S3Service()
router = APIRouter()

@router.post("/api/upload/presigned-url")
def generate_presigned_url(data: UploadRequest):

    allowed_extensions = [".docx", ".pptx"]

    allowed_types = [
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "application/vnd.openxmlformats-officedocument.presentationml.presentation"
    ]

    if not data.fileName.lower().endswith(tuple(allowed_extensions)):
        raise HTTPException(
            status_code=400,
            detail="Solo se permiten archivos DOCX y PPTX"
        )

    if data.fileType not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail="Tipo MIME no permitido"
        )
    if data.fileSize > 18 * 1024 * 1024:
        raise HTTPException(
            status_code=400,
            detail="El tamaño del archivo no puede exceder los 18 MB"
        )

    return s3_service.generate_presigned_url(
    data.fileName,
    data.fileType,
    data.fileSize
    
)