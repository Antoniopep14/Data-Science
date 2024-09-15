# para acceder a funciones dentro de paquetes usamos
import usuarios
from usuarios.moverse.moviendose import pagar_impuestos, guardar
guardar()
pagar_impuestos()
print(__name__)#__main__

# tambien es posible llamar a paquetes que estan es carpetas encima de la que estamos trabajando
# para ello escribimos un . por cada nivel que queramos subir
# from ..namecarpeta.namesubcarpeta.namearchivo import xfuncion
# esto de arriba se conoce como import relativo
#un import absoluto se hace mencionando el nombre del paquete
# from usuarios.acciones.utilidades import guardar
#cualquiera de las 2 es correcta, depende de cual te acomode mas

# al hace un import de usuarios y aplicarle dir
# ademas de los metodos magicos nos va a listar los subpaquetes dentro de usuarios (moverse)
print(dir(usuarios))
# ['__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'moverse']

# ahora veamos los metodos magicos de arriba
print(usuarios.__name__)  # nombre del paquete
print(usuarios.__package__)  # paquete perse
# print(usuarios.__path__)#ruta del paquete
print(usuarios.__file__)  # nombre del archivo al que hace referencia (init.py)
#c:\Users\anton\Documents\Proyectos-python\curso-py\modulos-07\usuarios\__init__.py
# Al usar __name__ y este indicarnos que es = __main__
# podemos usarlo para hacer tareas de mantenimiento en el paquete principal
# algo asi como:
if __name__ == "__main__":  # main es str, no olvidar eso
    print("realizando tarea de mantenimiento")
#tambien podemos hacer import condicional usando el if algo asi como
# if __name__ != "__main__":
     #from ..gestion.crud import guardar
     #print(__name__)

     #def pagar_impuestos():
         #print("pagando impuestos")
         #guardar()

#if __name__ == "__main__":
     #print("tarea de mantemiento")