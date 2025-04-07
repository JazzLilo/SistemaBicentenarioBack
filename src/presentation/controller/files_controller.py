from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
import os
from dotenv import load_dotenv
from pathlib import Path
import shutil
import uuid

# Cargar variables del .env
load_dotenv()

files_controller = APIRouter(prefix="/api/v1/files", tags=["Files"])

BASE_DIR = Path("public/imagenes")
BASE_URL = os.getenv("IP_FILES", "http://localhost:3000")

# Tipos válidos de carpeta
VALID_TYPES = {
    "presidente", "ubicacion", "cultura", "biblioteca",
    "usuario", "multimedia", "historia", "evento_Agendable","evento_h"
}

@files_controller.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    name: str = Form(None),
    tipo: str = Form(...)
):
    try:
        if tipo not in VALID_TYPES:
            raise HTTPException(status_code=400, detail="Tipo inválido")

        # Crear directorio si no existe
        upload_path = BASE_DIR / tipo
        upload_path.mkdir(parents=True, exist_ok=True)

        # Generar nombre único
        filename = f"{uuid.uuid4().hex}_{file.filename}"
        file_path = upload_path / filename

        # Guardar archivo
        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Generar URL
        file_url = f"{BASE_URL}/images/{tipo}/{filename}"

        return JSONResponse(
            status_code=200,
            content={
                "status": 200,
                "success": True,
                "message": "Archivo subido correctamente",
                "data": {
                    "file_url": file_url,
                    "name": name,
                    "tipo": tipo
                }
            }
        )

    except HTTPException as http_err:
        raise http_err
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"status": 500, "success": False, "error": str(e)}
        )
