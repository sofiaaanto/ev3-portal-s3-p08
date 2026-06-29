from pydantic import BaseModel

class FileRegister(BaseModel):
    key: str
    publicUrl: str
    fileName: str
    fileSize: int