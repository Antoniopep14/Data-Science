# #ahora veamos como enviar correos en html
# #para lo cual vamos a tener que escribir una plantilla en html
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import smtplib #para iniciar sesion en el servidor google
# from email.mime.image import MIMEImage #para mandar la imagen
# from pathlib import Path
# from string import Template #esto nos va a permitir reemplazar la variable usuarios en la plantilla


# plantilla = """
#     <b>Hola mundo! $usuario</b>
# """
# #se pueden tener muchas plantillas como $usuario $nombre $edad
# templa = Template(plantilla)
# # cuerpo = templa.substitute({ "usuario": "chanchito feliz" })
# ##ahora cambiaremos el nombre del usuario
# cuerpo = templa.substitute(usuario="chanchito feliz")

# path = Path("11-modulos-nativos/imagen correo.png")
# mime_image= MIMEImage(path.read_bytes())#se pasa la imagen en bytes no el path
# mensaje = MIMEMultipart()
# mensaje["from"] = "Hola Mundo"
# mensaje["to"] = "antonio.142103@gmail.com"
# mensaje["subject"] = "clave vscode app externa"
# cuerpo = MIMEText(cuerpo, "html")# su segundo parametro es plain por defecto, pero podriamos ponerle httml que veremos mas adelante
# mensaje.attach(cuerpo)#esto no recibe un str asi que tenemos que pasarle la instancia de mimetext
# mensaje.attach(mime_image)#para pasar varios elementos usamos varios attach
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
# #al ejecutar mande correo con la plantilla

#pero la plantilla no siempre va a estar dentro del mismo archivo
#sino que la vamos a tener que importar
#asi que creamos la platilla.html
#al apretar ! y seleccionar la primer opcion que da no escribe una plantilla
#que solo tendremos que llenar
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib #para iniciar sesion en el servidor google
from email.mime.image import MIMEImage #para mandar la imagen
from pathlib import Path
from string import Template #esto nos va a permitir reemplazar la variable usuarios en la plantilla

#ahora importamos la plantilla con una variable con el mismo nobre
plantilla = Path("11-modulos-nativos/plantilla.html").read_text("utf-8")
#si manda warning solo agregamos el tipo de codificacion utf-8
templa = Template(plantilla)
cuerpo = templa.substitute(usuario="chanchito feliz")
path = Path("11-modulos-nativos/imagen correo.png")
mime_image= MIMEImage(path.read_bytes())#se pasa la imagen en bytes no el path
mensaje = MIMEMultipart()
mensaje["from"] = "Hola Mundo"
mensaje["to"] = "antonio.142103@gmail.com"
mensaje["subject"] = "clave vscode app externa"
cuerpo = MIMEText(cuerpo, "html")# su segundo parametro es plain por defecto, pero podriamos ponerle httml que veremos mas adelante
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
#ejecutamos y se manda el correo
#tomar nota sobre que deje una lineas en la plantilla --rpe fuera del codigo
#y tambien se mandaron xD 