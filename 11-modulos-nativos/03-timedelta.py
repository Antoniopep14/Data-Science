#ahora trabajaremos con las diferencias en las fechas
from datetime import datetime, timedelta
fecha1 = datetime(2023, 1, 1) + timedelta(weeks=1)
fecha2 = datetime(2023, 2, 1)

delta = fecha2 - fecha1
print(delta)#31 days, 0:00:00
print("días", delta.days)
print("segundos", delta.seconds)
print("microsegundos", delta.microseconds)
print("total_seconds", delta.total_seconds())#este ultimo es un metodo por lo que tenemos que ejecutarlo
#31 days, 0:00:00
# días 31
# segundos 0
# microsegundos 0
# total_seconds 2678400.0

##al agregarle el time delta con un argumento el tiempo cambia
#entonces se entiende que con timedelta poedmos agregarle o quitarle tiempo a la fecha
#24 days, 0:00:00
# días 24
# segundos 0
# microsegundos 0
# total_seconds 2073600.0
