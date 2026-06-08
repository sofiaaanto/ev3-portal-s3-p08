import boto3

from config import AWS_REGION, AWS_BUCKET_NAME


class S3Service:

    def __init__(self):

        self.s3 = boto3.client(
            "s3",
            region_name=AWS_REGION
        )

    def generate_presigned_url(
        self,
        file_name: str,
        file_type: str
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