from io import open

# ESCRITURA
# primero creamos el texto que queremos agregar
# texto = "Hola mundo!"
# ahora creamos la referencia a nuestro archivo
# archivo = open("archivos/hola_mundo.txt", "w")
# y despues de referenciar al archivo
# tenemos que indicarle si queremos usarlo para escritura, lectura, etc
# "w" es para escritura, si el archivo al que estamos referenciando por alguna razon no existe
# python se va a encargar de crearlo
#ahora ya podemos escribir
# archivo.write(texto)
# archivo.close()  # Una desventaja de usar el metodo open, es que el archivo se queda ocupando memoria del ordenador
# y tenemos que cerrarlo con el metodo de close, al terminar de usarlo
# al ejecutar el codigo, creo el archivo con el texto indicado arriba
# lo comentamos todo y ahora vamos a llamar al metodo de lectura

# LECTURA
# la r es el argumento por defecto, por lo que si no ponemos nada lo tomara como si tuviera r
# archivo = open("archivos/hola_mundo.txt", "r")
# para que nosotros podamos leer el archivo
# tenemos que crear una variable la cual va a ser el texto que se va a encontar dentro del archivo
# texto = archivo.read()
# archivo.close()
# print(texto)
# una vez que le pasamos el texto a la variable, podemos cerrar el archivo
# y al llamar a print de texto nos va a pasar el contenido del archivo
# #nuevamente comentamos todo y ahora veamos otro metdo

# LECTURA COMO LISTA
# archivo = open("archivos/hola_mundo.txt", "r")
# texto = archivo.readlines()#solo se agrega readlines como metodo, y nos devuelve una lista del texto
# separando cada linea del archivo como elemento de la lista
# archivo.close()
# print(texto)
# #nuevamente comentamos

# ahora veamos algunos metodos magicos de la funcion de open
# archivo = open("archivos/hola_mundo.txt", "r")
# #WITH, SEEK
# with open("archivos/hola_mundo.txt", "r") as archivo:
#     # al usar esta instruccion de with, se va a encargar de abrir y cerrar el archivo de manera automatica sin que se lo indiquemos
#     # por alguna razon si hay un error al abrir un archivo y manda una excepcion
#     # podemos tratarla con try y except o usar el metodo with
#     print(archivo.readlines()) #esto carga todo el archivo en memoria
#     #para leer linea por linea lo que podriamos hacer con un metodo for
#     #for linea in archivo:
#           print(linea) #esto da un str
#   # si ejecutaramos los 2 prints de arriba solo nos daria el de la lista porque
#     # una vez que avanza con la instruccion with, ya no regresa por las lineas en las que ya paso, a menos que se lo indiquemos manualmente
#     #y eso se haria con el metodo seek
#     archivo.seek(0)##donde le indicamos el caracter (no linea, recuerda que es una lista) a donde queremos que se devuelva
# lo de arriba tendria que ir antes del for para que nos regrese a la primer linea

# # AGREGAR
# # ahora si solo queremos agregar una cosa a un archivo y no eliminar todo su contenido
# archivo = open("archivos/hola_mundo.txt", "a+")
# archivo.write("chao mundo :(")
# archivo.close()
# #al ejecutar agrega chao mundo al archivo de forma
# Hola mundo!chao mundo :(

# LECTURA Y ESCRITURA (ahora vamos a hacerlo simultaneamente)
# creamos la referencia al archivo
with open("archivos/hola_mundo.txt", "r+") as archivo:
    # esto va a leer todas las lineas del archivo y las va a agregar como una lista
    texto = archivo.readlines()
    # al ejecutar lo de arriba nos va a mover el puntero hasta el final
    # pero como queremos agregar algo al comienzo, vamos a mover el puntero al comienzo usando seek
    archivo.seek(0)
    texto[0] = "Chanchito feliz la"
    archivo.writelines(texto)
    # esto a diferencia de write nos va a permitir escribir una lista dentro de nuestro archivo
    # de manera que ya no es necesario iterar linea por linea para agregar el texto al archivo
    # ademas podemos pasarle la variable de texto sin encesidad de tener que transformala de nuevo a un string
# ahora tenemos Chanchito feliz mundo :( en el archivo, porque lo que hizo fue reemplazar hasta donde llego el str
# lo demas queda igual y debemos tener cuidado con eso
## al ejecutar con la al final nos da #Chanchito feliz lando :(
