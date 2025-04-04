import logging
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.presentation.controller.user_controller import user_controller
from src.presentation.controller.role_controller import rol_controller
from src.presentation.controller.user_role_controller import user_role_controller
from src.presentation.controller.auditoria_controller import auditoria_controller
from src.presentation.controller.presidente_controller import presidente_controller
from src.presentation.controller.ubicacion_controller import ubicacion_controller
from src.presentation.controller.evento_historico_controller import eventoHistorico_controller

logging.basicConfig(level=logging.DEBUG)    
logger = logging.getLogger(__name__)
load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_controller)
app.include_router(rol_controller)
app.include_router(user_role_controller)
app.include_router(auditoria_controller)
app.include_router(presidente_controller)
app.include_router(ubicacion_controller)
app.include_router(eventoHistorico_controller)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
