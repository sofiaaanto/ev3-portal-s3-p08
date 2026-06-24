import boto3
from botocore.client import Config
from datetime import datetime
from botocore.exceptions import ClientError

from app.config import (
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    AWS_SESSION_TOKEN,
    AWS_REGION,
    AWS_BUCKET_NAME
)

class S3Service:

    def __init__(self):


        self.s3 = boto3.client(
            "s3",
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            aws_session_token=AWS_SESSION_TOKEN,
            region_name=AWS_REGION,
            config=Config(signature_version="s3v4")
        )

    def generate_presigned_url(
        self,
        file_name: str,
        file_type: str,
        file_size: int
    ):

        key = f"uploads/{file_name}"

        presigned_url = self.s3.generate_presigned_url(
            ClientMethod="put_object",
            Params={
                "Bucket": AWS_BUCKET_NAME,
                "Key": key,
                "ContentType": file_type
            },
            ExpiresIn=300
        )

        public_url = (
            f"https://{AWS_BUCKET_NAME}.s3."
            f"{AWS_REGION}.amazonaws.com/{key}"
        )

        return {
            "presignedUrl": presigned_url,
            "key": key,
            "publicUrl": public_url
        }

    def list_files(self):

        response = self.s3.list_objects_v2(
            Bucket=AWS_BUCKET_NAME
        )

        archivos = []

        for obj in response.get("Contents", []):

            archivos.append({
                "id": obj["Key"],
                "nombre": obj["Key"].replace("uploads/", ""),
                "tamano": obj["Size"],
                "fecha": obj["LastModified"].isoformat()
            })

        return archivos

    def generate_presigned_get_url(self, file_name: str):
        presigned_url = self.s3.generate_presigned_url(
            ClientMethod="get_object",
            Params={
                "Bucket": AWS_BUCKET_NAME,
                "Key": file_name
            },
            ExpiresIn=300
        )

        return {"presignedUrl": presigned_url}

    def delete_file(self, file_name):

        self.s3.delete_object(
            Bucket=AWS_BUCKET_NAME,
            Key=file_name
        )

        return {"message": "Archivo eliminado"}

    def test_connection(self):
        try:
            self.s3.head_bucket(Bucket=AWS_BUCKET_NAME)
            return {"status": "ok"}
        except Exception as e:
            return {"error": str(e)}