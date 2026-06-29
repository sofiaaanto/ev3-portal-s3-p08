from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import boto3

from app.routes.upload import router as upload_router
from app.routes.dynamodb import router as dynamodb_router

from app.config import (
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    AWS_SESSION_TOKEN,
    AWS_REGION,
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router)
app.include_router(dynamodb_router)

@app.get("/")
def home():
    return {"mensaje": "Backend funcionando"}

@app.get("/healthz")
def health():
    return {"status": "ok"}

# Prueba de conexión con DynamoDB
session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    aws_session_token=AWS_SESSION_TOKEN,
    region_name=AWS_REGION,
)

dynamodb = session.resource("dynamodb")
table = dynamodb.Table("database_dynamo")

table.put_item(
    Item={
        "id_tabla": "1",
        "p08_proyecto": "P08",
        "nombre_proyecto": "Prueba",
        "descripcion": "Conexión exitosa"
    }
)

print("Data uploaded successfully to DynamoDB.")