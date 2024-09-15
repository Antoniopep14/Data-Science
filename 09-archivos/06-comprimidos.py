# Ahora aprenderemos a trabajar con archivos comprimidos, en especifico con los archivos zip
from pathlib import Path
# ahora importamos un modulo para poder comprimir los archivos
from zipfile import ZipFile
# #ESCRIBIR
# # al igual que el metodo de path debemos usar el metodo de with para poder trabajar con los archivos comprimidos en zip
# # + el modo w para crear el archivo comprimido
# with ZipFile("archivos/comprimidos.zip", "w") as zip:
#     # el archivo aun no esta creado, y lo llamamos zip como referencia en el futuro
#     # recordar que para trbajar con todo esto debemos estar dentro de la carpeta curso.py
#     for path in Path().rglob("*.*"):  # el rglob es para indicar que queremos ver los archivos de manera recursiva
#         # y *.* indica que queremos absulutamente todo
#         # el primer * indica que va a ser cualquier archivo con cualquier nombre y el segundo * indica cualquier extension
#         # el problema con esto es que entrariamos en un loop infinito, porque al incluir todos los archivos de curso.py
#         # tambien incluiremos el archivo zip, entonces tenemos que excluirlo
#         print(path)
#         #path es un objeto, asi que debemos transformalos para porder exluir el archivo zip
#         if str(path) != "archivos\comprimidos.zip":
#         #aqui pusimos \ en lugar de / porque la ruta en windows usa \
#         #y como estamos usando un str el / es el que me causaba muchos errores
#             zip.write(path)
# # #al ejecutar nos crea un archivo comprimido con todo lo que esta en curso-py

# # LEER de archivos comprimidos
with ZipFile("archivos/comprimidos.zip") as zip:
    #print(zip.namelist())
    # esto nos devuelve todos los archivos de todo lo que esta dentro del archivo comprimido
   
    # si queremos informacion especifica de algun archivo usamos el sig metodo
    # para este caso accederemos al mismo archivo donde estamos ahora
    info = zip.getinfo("archivos/06-comprimidos.py")
    print(
        info.file_size,  # nos da el tamaño del archivo
        info.compress_size  # nos da el tamaño de compresion
    )
    #2189 2189
    # para extraer todo lo que esta dentro del archivo usamos el siguiente metodo
    #donde le tenemos que indicar en donde queremos extraerlos
    zip.extractall("archivos/descomprimidos")
    # esto me crearia una carpeta llamada descomprimidos dentro de archivos
    # con todos los archivos comprimidos
