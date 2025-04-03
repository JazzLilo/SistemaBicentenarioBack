def verify_mail(verification_code):
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
    return subject, html_content

def recuperacion_pass(verification_code):
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
    return subject, html_content