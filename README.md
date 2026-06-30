# ArchivaCloud P-08

Integrantes:
- Mauricio Catalán Medina
- Sofía González Pradenas


# Descripción

ArchivaCloud es una aplicación web desarrollada para la asignatura **Arquitectura de Almacenamiento de Datos**.

El sistema permite almacenar documentos utilizando **Amazon S3** y registrar sus metadatos en **Amazon DynamoDB**. El frontend está desarrollado con **React + Vite** y el backend con **FastAPI**, el cual genera **Presigned URLs** para que los archivos sean cargados directamente a Amazon S3 sin exponer credenciales AWS.

**Región AWS:** `us-east-1`

**Bucket:** `archivacloud-p08-useast-1`

---

# Arquitectura

```text
                 Usuario
                    │
                    ▼
           React + Vite
                    │
               HTTP/JSON
                    │
                    ▼
              FastAPI API
               │        │
               ▼        ▼
         Amazon S3   Amazon DynamoDB
          Archivos      Metadatos
```

# Tecnologías

## Frontend

- React
- Vite
- JavaScript
- HTML5
- CSS3

## Backend

- FastAPI
- Uvicorn
- boto3
- Pydantic
- python-dotenv

## AWS

- Amazon S3
- Amazon DynamoDB
- IAM
- Presigned URLs

---

# Instalación

## Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Crear `.env`

```env
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_SESSION_TOKEN=
AWS_REGION=us-east-1
AWS_BUCKET_NAME=archivacloud-p08-useast-1
```

Ejecutar:

```bash
uvicorn app.main:app --reload
```

## Frontend

```bash
cd frontend
npm install
npm run dev
```

---

# Funcionalidades

## Amazon S3

- Generación de Presigned URLs.
- Subida segura de archivos.
- Validación de extensiones.
- Validación de tamaño máximo (18 MB).

## Amazon DynamoDB

- Registro de metadatos.
- Consulta de registros.
- Persistencia de información de archivos.

## Backend

- API REST con FastAPI.
- Variables de entorno.
- Logging.
- Health Check.
- Integración con AWS.

## Frontend

- Interfaz React.
- Comunicación con API.
- Gestión de carga de archivos.

---

# Seguridad

| Control | Implementación | Estado |
|---------|----------------|--------|
| SEC-01 | Variables de entorno | ✅ |
| SEC-02 | CORS restringido | ✅ |
| SEC-03 | Validación de archivos | ✅ |
| SEC-04 | Límite 18 MB | ✅ |
| SEC-05 | IAM mínimo privilegio | ⚠ Evidencia AWS |
| SEC-06 | Block Public Access | ⚠ Evidencia AWS |
| SEC-07 | Manejo seguro de errores | ✅ |
| SEC-08 | Cifrado S3 | ⚠ Evidencia AWS |
| SEC-09 | npm audit / pip-audit | ✅ |
| SEC-10 | HTTPS mediante Presigned URLs | ✅ |

---

# Variables de entorno

| Variable | Descripción |
|----------|-------------|
| AWS_ACCESS_KEY_ID | Access Key |
| AWS_SECRET_ACCESS_KEY | Secret Key |
| AWS_SESSION_TOKEN | Token temporal |
| AWS_REGION | Región AWS |
| AWS_BUCKET_NAME | Bucket S3 |

---

# Auditoría

Se realizaron auditorías utilizando:

```bash
npm audit
pip-audit
```

Las dependencias del backend corresponden únicamente a las declaradas en `requirements.txt`.

---

# Estructura

```text
ev3-portal-s3-p08
│
├── backend
│   ├── app
│   ├── requirements.txt
│   ├── .env
│   └── ...
│
├── frontend
│   ├── src
│   ├── public
│   ├── package.json
│   └── ...
```

---

# Evidencias

Agregar capturas de:

- Frontend funcionando.
- Backend.
- Swagger.
- Bucket S3.
- Tabla DynamoDB.
- Elementos DynamoDB.
- Block Public Access.
- IAM.
- Cifrado S3.


# Mejoras Futuras

- Búsqueda de documentos.
- Historial de operaciones.


# Licencia

Proyecto desarrollado con fines académicos para INACAP.