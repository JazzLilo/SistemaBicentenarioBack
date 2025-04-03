import secrets
import string
from src.core.repositories.usuario_repository import UsuarioRepository
from src.core.services.auth.mail_service import MailService
from src.responses.response import Response

class VerificationService:
    def __init__(self, usuario_repo: UsuarioRepository):
        self.usuario_repo = usuario_repo

    async def generate_and_send_code(self, email: str) -> Response:
        # Generar código de 6 dígitos
        code = ''.join(secrets.choice(string.digits) for _ in range(6))
        
        # Actualizar usuario con el código
        response = await self.usuario_repo.update_verification_code(email, code)
        if not response.success:
            return response
        
        # Enviar correo
        success, message = MailService.send_verification_email(email, code, "register")
        if not success:
            return Response(
                status=500,
                success=False,
                message=f"Error al enviar correo: {message}"
            )
        
        return Response(
            status=200,
            success=True,
            message="Código generado y enviado correctamente"
        )

    async def verify_code(self, email: str, code: str) -> Response:
        response = await self.usuario_repo.get_by_email(email)
        if not response.success:
            return response
        
        usuario = response.data
        if usuario.codeValidacion != code:
            return Response(
                status=400,
                success=False,
                message="Código de verificación incorrecto"
            )
        
        return Response(
            status=200,
            success=True,
            message="Código verificado correctamente"
        )