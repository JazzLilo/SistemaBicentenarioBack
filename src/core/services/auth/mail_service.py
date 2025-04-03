import logging
from typing import Tuple
from src.core.models.usuario_domain import UsuarioInDB

logger = logging.getLogger("backend")

class MailService:
    @staticmethod
    def send_verification_email(email: str, code: str, purpose: str) -> Tuple[bool, str]:
        """
        Simula el envío de un correo de verificación
        En producción se conectaría a un servicio real como SendGrid, Mailgun, etc.
        """
        try:
            logger.info(f"Enviando código {code} a {email} para {purpose}")
            # Aquí iría la lógica real de envío de correo
            return True, "Correo enviado exitosamente"
        except Exception as e:
            logger.error(f"Error al enviar correo a {email}: {str(e)}")
            return False, str(e)