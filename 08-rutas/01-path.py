from pathlib import Path 
# Esta clase  de path sirve para que podamos referenciar una ruta del computador
# Es importantwe saber que no es necesario que la ruta exista
# para crear una ruta hacemos lo siguiente
# para windows se debe escribir r que es raw string 
# y sirve para que no nos tome los \ como caracter de escape
# Path(r"C\Archivos de Programa\Minecraft")
# # Pero cuando programes usualmente tambien vas a usar servideres en Linux
# # por lo que tenemos que aprender a usar las rutas de Linux
# # para mac o linux se hace de la sig manera
# # Esto es una ruta absoluta, seria el equivalente de C:\archivos de programa\Minecraft
# Path("/usr/bin")
# Path()  # Esto va a crear un path a donde nos ecnontremos
# #users/home/mi_app por ejemplo
# Path.home()  # Crea una ruta a la carpeta de inicio del usuario
# # y tambien generar rutas a archivos por ejemplo:
# Path("one/__init__.py")  # Esta es una ruta relativa
# #es decir, en la carpeta donde me encuentro aprovecha de agregar ini al final
# # lo que va a hacer es aregar el one a la capeta donde nos encontramos

path = Path("hola-mundo/mi-archivo.py")  # esta carpeta  podria o no existir
# ahora veamos los metodos de path
path.is_file()  # se usa para saber si es un archivo
path.is_dir()  # se usa para saber si es una carpeta
path.exists()  # se usa para saber si existe

print(
    path.name,  # da nombre del archivo incluyendo la extension mi-archivo.py
    path.stem,  # nombre de archivo sin exrtension mi-archivo
    path.suffix,  # da la extension .py
    path.parent,  # da el directorio padre de donde estamos generando la ruta #hola-mundo
    path.absolute()  # da la ruta competa de donde se encontraria el path
)  # da C:\Users\anton\OneDrive\Documents\Proyectos python\hola-mundo\mi-archivo.py
#en mac seria algo asi como /Users/nicolasschurmann/workspace/curso-py/rutas/hola-mundo/mi-archivo.py

#TOMAR EN CUENTA QUE PARA WINDOWS SE USAN \ Y PARA MAC O LINUX /

# este metodo nos permite cambiarle el nombre al archivo, incluyendo la extension
p = path.with_name("chanchito.py")
print(p)#hola-mundo\chanchito.py
p = path.with_suffix(".bat")  # permite cambiar la extension
print(p)#hola-mundo\mi-archivo.bat
# con esto cambiamos el nombre del archivo sin su extension
p = path.with_stem("feliz")
print(p)#hola-mundo\feliz.py
