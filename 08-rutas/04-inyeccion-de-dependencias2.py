#AHORA VAMOS A APLICAR LA INYECCION DE DEPENDENCIAS
#es buena idea usarlos si los proyectos empiezan a crecer, sobretodo si tenemos que hacerles test 
#de manera periodica a estos
#la gran mayoria de los frameworks ya tiene implementada una solucion de inyeccion de dependencias
#pero vamos a ver como se hace utilizando lo aprendido de path y directorios

#lo primero que tenemos que hacer es entrar a la carpeta de rutas
#para lo cual abriremos el menu file, open folder y seleccionamos la carpeta
# a la izq nos a aparecer solo lo de rutas ahora
#y esto lo hacemos para que cuando ejecutemos la consola el codigo funcione
#porque se va a ejecutar de manera relativa al path donde nos encontramos

#lo que vamos a hacer ahora es importar los paquetes de uno y dos
#ademas queremos poder ejecutar los init de cada paquete dentro de este codigo

#para ello creamos los paquetes uno y dos con la sig sintaxis:
#def init():
    #print("soy paquete uno") #con uno y dos respectivamente

#primero importamos path y creamos la variable de path
from pathlib import Path

#### LA FORMA EN QUE DEBERIAMOS DE GENERAR NUESTRO DICCIONARIO DE DEPENDENCIAS DENTRO DE NUESTRO ARCHIVO PRINCIPAL
#### TENEMOS QUE IMPORTAR LAS BASES DE DATOS DESDE EL INICIO
#### por ejemplo
# from db import db
# #tambien puede ser solo
# import db
# import graphql
# import api

####y ya solo tendiramos que modificar las dependencias:
####dependencias = {"db": db, "api": api, "graphql": graphql}

path = Path()#esta variable va a ser en base a la ruta en la cual nos encontramos actualmente
#y ahora creamos ubna lista de paths en base a una lista de comprension
paths = [p for p in path.iterdir() if p.is_dir()]
#para que solo muestre los directorios y no todo
#ahora vamos a iterar esos paths con una funcion llamada load
#la cual se va a encargar de tomar cada uno de estos paths e importarlos
#ademas de ejecutar el metodo de init

###UNA VEZ COLOCADOS LOS TRY Y EXCEPT 
###tenemos que definir la dependencias para pasarselas a init
dependencias = {
    "db": "base de datos", #esta es la conexcion a la base de datos
    "api": "esta es la api", #a la api
    "graphql": "esto es fraphql" #por si llegaramos a crear un graphql
}

#definimos la funcion de load, la cual a a recibir un path
def load(p):
    ##para continuar primero vamos a ver que contiene p
    ##print(str(p))
    ##podria ser que nosotros queremos cargar todos los modulos de p de manera recursiva
    ##para ello tendriamos que reemplar todos los / dentro de p por un .
    ##porque hay que recordad que p va a venir con una ruta osea /
    ##para ello tendriamos que poner
    ##print(str(p).replace("/", "."))
    ## COMENTAMOS LO ANTERIOR JUNTO A LIST(MAP)
    ##y agreamos todo al import de abajo
    #aqui vamos a comenzar a importar nuestro paquetes
    #usaremos la funcion import que nos ayuda a importar paquetes y modulos de manera dinamica
    paquete = __import__(str(p).replace("/", "."))
    #ahora ejecutamos la funcion de init con cada uno de los paquetes
    try:
        ###paquete.init()
        ###ahora utilizando el operador de empaquetamiento o desempaquetamiento le pasamos la dependencias
        paquete.init(**dependencias)
        ###AHORA TENEMOS QUE IR A MODULO UNO Y DOS
        ###y sacar las dependencias que necesitamos
        ###les aplicamos la modificacion que tienen actualmente
    except:
        print("el paquete no tiene funcion init")

#para ver que contiene p primero tenemos que convertir la funcino map en una lista
list(map(load, paths)) #dos,   uno,  __pycache__
#si no lo convertimos en una lista no va a ejecutar nada
#map(load, paths)

#al ejecutar nos va a dar #soy modulo dos, soy modulo uno
#y un error porque el paquete de dependencias 2 no tiene un metodo de init
#esto podria pasar con varios paquetes
#para lo cual vamos a agregar un try para fallar elegantemente

###al ejecutar despues de las modificaciones nos va a dar
#soy modulo dos: base de datos esta es la api,    soy modulo uno: esto es fraphql
#el paquete no tiene funcion init