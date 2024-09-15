# import time
# print(time.time())#nos da un timestamp que es el timepo transcurrido desde el 1 de enero de 1970
# #1702139792.416075
# #UTC: coordinated universal time, UTC 0 es en Grennwich England

# import datetime#nos da algo mas legible pero es tedioso
# fecha = datetime.datetime(2023, 1, 1)
# print(fecha)#2023-01-01 00:00:00
#la mejor forma de usarlo es la siguiente
from datetime import datetime
fecha = datetime(2023, 1, 1)
fecha2 = datetime(2023, 2, 1)
#print(fecha)#2023-01-01 00:00:00

ahora = datetime.now()
#print(ahora)#2023-12-09 10:42:16.091822

#ahora crearemos fechas a partir de str
fechaStr = datetime.strptime("2023-01-02", "%Y-%m-%d")
#podriamos haber usado / u otra cosa, despues de la fecha indicamos como queremos
#que python interprete esa fecha usando directives
#print(fechaStr)#2023-01-02 00:00:00

# si queremos conocer todos los directives de strtime podemos ir a 
#https://docs.python.org/3/library/datetime.html
#y buscar directive

#ahora crearemos un str a partir de una fecha
#print(fecha.strftime("%Y.%m.%d"))#2023.01.01

#tambien podemos comparar fechas
#print(fecha > fecha2)#false

#ahora veamos las propiedades de fecha
print(
    fecha.year,
    fecha.month,
    fecha.day,
    fecha.hour,
    fecha.minute,
)#2023 1 1 0 0




