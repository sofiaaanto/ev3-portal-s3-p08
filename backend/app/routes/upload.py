from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse
from app.models.upload_request import UploadRequest
from app.services.s3_service import S3Service
from app.models.file_register import FileRegister
from app.services.dynamodb_service import DynamoDBService


s3_service = S3Service()
dynamo = DynamoDBService()
router = APIRouter()

@router.get("/api/test")
def test():
    return s3_service.test_connection()

@router.get("/api/files")
def get_files():

    return s3_service.list_files()


@router.delete("/api/files/{file_name:path}")
def delete_file(file_name: str):

    # 1. borrar S3
    s3_service.delete_file(file_name)

    # 2. borrar DynamoDB
    dynamo.eliminar_archivo(file_name)

    return {"message": "Archivo eliminado"}

@router.get("/api/files/{file_name:path}/download")
def download_file(file_name: str):
    presigned = s3_service.generate_presigned_get_url(file_name)
    return RedirectResponse(presigned["presignedUrl"])

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


@router.post("/api/files/register")
def register_file(data: FileRegister):

    return dynamo.guardar_archivo(data)