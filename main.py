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
from src.presentation.controller.categoria_controller import categoria_controller
from src.presentation.controller.c_h_controller import categoriaHistoria_controller
from src.presentation.controller.multimedia_controller import multimedia_controller
from src.presentation.controller.evento_agendable_controller import evento_agendable_controller
from src.presentation.controller.participante_evento_controller import participante_evento_controller
from src.presentation.controller.agenda_usuario_controller import agenda_usuario_controller
from src.presentation.controller.historia_controller import historia_controller
from src.presentation.controller.cultura_controller import cultura_controller
from src.presentation.controller.biblioteca_controller import biblioteca_controller
from src.presentation.controller.comentario_controller import comentario_controller
from src.presentation.controller.files_controller import files_controller	

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
app.include_router(categoria_controller)
app.include_router(categoriaHistoria_controller)
app.include_router(multimedia_controller)
app.include_router(evento_agendable_controller)
app.include_router(participante_evento_controller)
app.include_router(agenda_usuario_controller)
app.include_router(historia_controller)
app.include_router(cultura_controller)
app.include_router(biblioteca_controller)
app.include_router(comentario_controller)
app.include_router(files_controller)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
