# los modulos se usan para poder tomar codigo reelevante entre si y guardarlo en archivos diferentes
# nos a yudan a ser mas ordenados
# vamos a importar funciones que tenemos en usuarios
from usuario_impuestos import guardar, pagar_impuestos
# si presionamos ctrl + space, nos da sugerencias
# from usuarios import *  importaria todo, pero debemos tener cuidado de no tener 2 funciones, metodos, etc iguales
# al importar eso ya podemos ejecutar la funcion guardar aqui
# la forma correcta (conevncion) de guardar archivos debe ser con _
# para seguir el orden de la correcta sintaxis de python
guardar()  # estamos llamando la funcion de usuarios
pagar_impuestos()

#los archivos de pycache son archivos compilados que importamos
#python los compila para poder llamarlos mas tarde de forma mas rapida

# PAQUETES
# la dif con los modulos es que los modulos apuntan a archivos y los paquetes a carpetas
# para convertir una carpeta en un paquete debemos crear un archivo dentro llamado __init__.py
# para llamar a la carpeta usamos namecarpeta.namearchivo
# import usuarios.acciones
# pero a la hora de escribir codigo nos daria mas problemas porque
# tendriamos que escribirlo de la sig manera
# usuarios.acciones.guardar()
# otra forma de llamarlo es asi
# from usuarios import acciones
# acciones.guardar()
# otra forma es
# from usuarios.acciones import guardar
# guardar()

## AHORA SUPONGAMOS QUE NUESTRO CODIGO CRECIO MUCHO Y QUEREMOS HACER SUBCARPETAS
#movimos acciones a carpeta acciones, renombramos por utilidades y creamos __init__.py
#ahora tendriamos que llamarlo de la sig manera
from usuarios.acciones.utilidades import guardar

