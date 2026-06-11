import boto3
from botocore.client import Config

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