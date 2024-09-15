# #para enviar correos haremos uso de SMTP
# #simple mail  transfer protocol
# #que es el usado para gmail
# #pero desde 2l 2022 gmail no permite su uso sin antes habilitar una opcion
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import smtplib #para iniciar sesion en el servidor google
# #MIME: multipurpose intenet mail extension
# mensaje = MIMEMultipart()
# mensaje["from"] = "Hola Mundo"
# mensaje["to"] = "antonio.142103@gmail.com"
# mensaje["subject"] = "clave vscode app externa"
# cuerpo = MIMEText("obam vbkf qiro nzti")# su segundo parametro es plain por defecto, pero podriamos ponerle httml que veremos mas adelante
# mensaje.attach(cuerpo)#esto no recibe un str asi que tenemos que pasarle la instancia de mimetext
# #ahora definimos donde se encontrara nuestro servidor SMTP
# #aqui es necesario cerrar la conexion siempre asi que podemos usar el metodo with
# with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
#     #ahora tenemos que identificarnos
#     smtp.ehlo()
#     #ahora tenemos que indicar el encriptado que usaremos para enviar correos
#     smtp.starttls()

#     #ahora iniciaremos sesion en el servidor de google
#     smtp.login("antonio.142103@gmail.com", "obam vbkf qiro nzti")
#     smtp.send_message(mensaje)
# #al ejecutar me mande el correo con la clave de vscode

#ahora hagamos lo mismo enviando una imagen
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib #para iniciar sesion en el servidor google
from email.mime.image import MIMEImage #para mandar la imagen
from pathlib import Path
#MIME: multipurpose intenet mail extension
path = Path("11-modulos-nativos/imagen correo.png")
mime_image= MIMEImage(path.read_bytes())#se pasa la imagen en bytes no el path
mensaje = MIMEMultipart()
mensaje["from"] = "Hola Mundo"
mensaje["to"] = "antonio.142103@gmail.com"
mensaje["subject"] = "clave vscode app externa"
cuerpo = MIMEText("obam vbkf qiro nzti")# su segundo parametro es plain por defecto, pero podriamos ponerle httml que veremos mas adelante
mensaje.attach(cuerpo)#esto no recibe un str asi que tenemos que pasarle la instancia de mimetext
mensaje.attach(mime_image)#para pasar varios elementos usamos varios attach
#ahora definimos donde se encontrara nuestro servidor SMTP
#aqui es necesario cerrar la conexion siempre asi que podemos usar el metodo with
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    #ahora tenemos que identificarnos
    smtp.ehlo()
    #ahora tenemos que indicar el encriptado que usaremos para enviar correos
    smtp.starttls()

    #ahora iniciaremos sesion en el servidor de google
    smtp.login("antonio.142103@gmail.com", "obam vbkf qiro nzti")
    smtp.send_message(mensaje)
#de esta manera me envie la imagen al ejecutar
