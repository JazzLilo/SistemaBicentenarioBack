import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_email_via_smtp():
    # Configuración SMTP
    smtp_server = "smtp-relay.brevo.com"
    port = 587
    username = "8947ed001@smtp-brevo.com"
    password = "AwyK42xGCkJVZROQ"  # Considera usar variables de entorno
    
    # Datos del correo
    sender_email = "eljudionaci234@gmail.com"  # Debe estar verificado en Brevo
    receiver_email = "vjoelsuxod@gmail.com"  # Cambiar por un email real
    subject = "Prueba SMTP con Brevo"
    
    # Cuerpo del mensaje
    html_content = """
    <html>
      <body>
        <h1 style="color: #0066cc;">¡Prueba exitosa!</h1>
        <p>Este correo fue enviado usando el servidor SMTP de Brevo.</p>
        <p><strong>Credenciales usadas:</strong></p>
        <ul>
          <li>Servidor: smtp-relay.brevo.com</li>
          <li>Puerto: 587</li>
          <li>Identificador: 8947ed001@smtp-brevo.com</li>
        </ul>
      </body>
    </html>
    """
    
    # Crear mensaje
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(html_content, "html"))
    
    try:
        # Iniciar conexión segura
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(username, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        
        print("¡Correo enviado exitosamente via SMTP!")
        return True
    
    except Exception as e:
        print(f"Error al enviar correo: {str(e)}")
        return False

if __name__ == "__main__":
    # Mejora: Usar variables de entorno para las credenciales
    # os.environ["BREVO_SMTP_USER"] = "8947ed001@smtp-brevo.com"
    # os.environ["BREVO_SMTP_PASSWORD"] = "AwyK42xGCkJVZROQ"
    
    print("Probando envío SMTP con Brevo...")
    send_email_via_smtp()