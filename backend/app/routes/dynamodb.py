from fastapi import APIRouter
from app.services.dynamodb_service import DynamoDBService

router = APIRouter(prefix="/dynamodb", tags=["DynamoDB"])

service = DynamoDBService()

@router.post("/upload")
def subir_datos():

    data = [
    {
        "id_tabla": "1",
        "p08_proyecto": "P08",
        "nombre_proyecto": "Item1",
        "descripcion": "Descripcion1"
    },
    {
        "id_tabla": "2",
        "p08_proyecto": "P08",
        "nombre_proyecto": "Item2",
        "descripcion": "Descripcion2"
    }
]


    return service.guardar(data)