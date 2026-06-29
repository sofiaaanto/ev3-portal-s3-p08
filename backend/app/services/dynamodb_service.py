import os
import boto3
from dotenv import load_dotenv
from datetime import datetime
from app.config import AWS_BUCKET_NAME

load_dotenv()

class DynamoDBService:


    def __init__(self):

        session = boto3.Session(
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            aws_session_token=os.getenv("AWS_SESSION_TOKEN"),
            region_name=os.getenv("AWS_REGION")
        )

        dynamodb = session.resource("dynamodb")
        self.table = dynamodb.Table(os.getenv("DYNAMODB_TABLE"))

        # NUEVO: cliente de S3 con la misma sesión
        self.s3 = session.client("s3")

    def guardar_archivo(self, data):

        key = data.key  # uploads/archivo.docx

        self.table.put_item(
            Item={
                "id_tabla": key,
                "p08_proyecto": "P08",
                "nombre_archivo": data.fileName,
                "url": data.publicUrl,
                "tamano": data.fileSize,
                "fecha": datetime.now().isoformat()
            }
        )

        return {"mensaje": "Archivo registrado"}

    def eliminar_archivo(self, file_name):
        try:
            self.table.delete_item(
                Key={
                    "id_tabla": file_name,
                    "p08_proyecto": "P08"
                }
            )

            self.s3.delete_object(
                Bucket=AWS_BUCKET_NAME,
                Key=file_name
            )

            return {"message": "OK"}

        except Exception as e:
            raise Exception(f"Error al eliminar archivo: {str(e)}")