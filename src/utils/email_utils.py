import random
import string
import logging
import os
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pydantic import EmailStr
from pprint import pprint

logger = logging.getLogger("backend")

# Función para generar código aleatorio de 6 caracteres (letras mayúsculas y números)
def generate_verification_code(length=6):
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Configuración de Brevo (anteriormente Sendinblue)
def configure_brevo_api():
    configuration = sib_api_v3_sdk.Configuration()
    api_key = os.environ.get("BREVO_API_KEY")
    configuration.api_key['api-key'] = api_key
    return configuration

# Función para crear campañas de correo
def create_email_campaign(name: str, subject: str, html_content: str, list_ids: list, scheduled_at: str = None):
    try:
        configuration = configure_brevo_api()
        api_instance = sib_api_v3_sdk.EmailCampaignsApi(sib_api_v3_sdk.ApiClient(configuration))
        
        email_campaigns = sib_api_v3_sdk.CreateEmailCampaign(
            name=name,
            subject=subject,
            sender={"name": "SEGURIDAD INFORMÀTICA - LA PAZ BOLIVIA", "email": "mentoresjulio@gmail.com"},
            type="classic",
            html_content=html_content,
            recipients={"listIds": list_ids},
            scheduled_at=scheduled_at
        )
        
        api_response = api_instance.create_email_campaign(email_campaigns)
        logger.info(f"Campaña de correo creada exitosamente: {name}")
        return True, api_response
        
    except ApiException as e:
        logger.error(f"Error al crear campaña de correo: {str(e)}")
        return False, str(e)

# Función para enviar correo de verificación
def send_verification_email(email: EmailStr, verification_code: str, template_type: str = "register"):
    try:
        # Configuración de la API
        configuration = configure_brevo_api()
        api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
        
        # Determinar el asunto y contenido según el tipo de template
        if template_type == "register":
            subject = "Verificación de correo - Bicentenario Bolivia"
            html_content = f"""
            <html>
                <body style="font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f9f9f9;">
                    <div style="max-width: 600px; margin: 0 auto; background-color: #ffffff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1);">
                        <div style="text-align: center; border-bottom: 5px solid #ffdd00;">
                            <div style="background: linear-gradient(to bottom, #d52b1e 33%, #ffdd00 33%, #ffdd00 66%, #007934 66%); height: 15px; margin-bottom: 20px;"></div>
                            <h1 style="color: #d52b1e; margin: 0; padding: 10px 0;">Bicentenario de Bolivia</h1>
                            <p style="color: #007934; font-style: italic; margin: 5px 0 15px 0;">200 años de historia y cultura</p>
                        </div>
                        
                        <div style="padding: 20px 0; text-align: center;">
                            <h2 style="color: #333;">¡Bienvenido a Nuestra Plataforma Cultural!</h2>
                            <p style="color: #555; line-height: 1.5;">Gracias por formar parte de la celebración de nuestros 200 años de independencia. Para completar su registro y participar en nuestros eventos culturales y folklóricos, por favor utilice el siguiente código de verificación:</p>
                            
                            <div style="background: linear-gradient(45deg, #d52b1e, #ffdd00, #007934); padding: 3px; margin: 25px auto; width: 200px; border-radius: 8px;">
                                <div style="background-color: white; padding: 15px; border-radius: 5px; text-align: center;">
                                    <h2 style="font-size: 28px; letter-spacing: 5px; margin: 0; color: #333;">{verification_code}</h2>
                                </div>
                            </div>
                            
                            <p style="color: #777; font-size: 14px;">El código es válido por 10 minutos.</p>
                        </div>
                        
                        <div style="text-align: center; margin-top: 30px; padding-top: 20px; border-top: 1px solid #eee;">
                            <p style="color: #666; font-size: 14px;">Celebrando nuestra herencia cultural y folklórica</p>
                            <div style="background: linear-gradient(to bottom, #d52b1e 33%, #ffdd00 33%, #ffdd00 66%, #007934 66%); height: 10px; margin-top: 15px;"></div>
                        </div>
                    </div>
                </body>
            </html>
            """
        else:  # forgotPassword
            subject = "Recuperación de contraseña - Bicentenario Bolivia"
            html_content = f"""
            <html>
                <body style="font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f9f9f9;">
                    <div style="max-width: 600px; margin: 0 auto; background-color: #ffffff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1);">
                        <div style="text-align: center; border-bottom: 5px solid #ffdd00;">
                            <div style="background: linear-gradient(to bottom, #d52b1e 33%, #ffdd00 33%, #ffdd00 66%, #007934 66%); height: 15px; margin-bottom: 20px;"></div>
                            <h1 style="color: #d52b1e; margin: 0; padding: 10px 0;">Bicentenario de Bolivia</h1>
                            <p style="color: #007934; font-style: italic; margin: 5px 0 15px 0;">200 años de historia y cultura</p>
                        </div>
                        
                        <div style="padding: 20px 0; text-align: center;">
                            <h2 style="color: #333;">Recuperación de Contraseña</h2>
                            <p style="color: #555; line-height: 1.5;">Para continuar disfrutando de nuestros eventos culturales y folklóricos conmemorativos de los 200 años de Bolivia, utilice este código para restablecer su contraseña:</p>
                            
                            <div style="background: linear-gradient(45deg, #d52b1e, #ffdd00, #007934); padding: 3px; margin: 25px auto; width: 200px; border-radius: 8px;">
                                <div style="background-color: white; padding: 15px; border-radius: 5px; text-align: center;">
                                    <h2 style="font-size: 28px; letter-spacing: 5px; margin: 0; color: #333;">{verification_code}</h2>
                                </div>
                            </div>
                            
                            <p style="color: #777; font-size: 14px;">Si es un error, obvie este email, de ser correcto el envío, no comparta con nadie su código.</p>
                        </div>
                        
                        <div style="text-align: center; margin-top: 30px; padding-top: 20px; border-top: 1px solid #eee;">
                            <p style="color: #666; font-size: 14px;">Celebrando el patrimonio y la diversidad cultural de Bolivia</p>
                            <div style="background: linear-gradient(to bottom, #d52b1e 33%, #ffdd00 33%, #ffdd00 66%, #007934 66%); height: 10px; margin-top: 15px;"></div>
                        </div>
                    </div>
                </body>
            </html>
            """
        
        # Crear el correo con los datos proporcionados
        sender = {
            "name": os.environ.get("SENDER_NAME"),
            "email": os.environ.get("SENDER_EMAIL")
        }
        to = [{"email": email}]
        
        send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
            to=to,
            sender=sender,
            subject=subject,
            html_content=html_content
        )
        
        # Enviar el correo
        response = api_instance.send_transac_email(send_smtp_email)
        logger.info(f"Correo de verificación enviado a {email} con código {verification_code}")
        return True, response
        
    except ApiException as e:
        logger.error(f"Error al enviar correo: {str(e)}")
        return False, str(e)
