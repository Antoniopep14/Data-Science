# las filas tienen la caracteristica de ser FiFo
# first in first out, es decir el primero que llega es el primero que se va
# una lista muy larga podemos sobresaturar la PC o servidor
# lista = list(range(100000000))
# para ello podemos importar un modulo
from collections import deque

fila = deque([1, 2])  # deque es una clase
# y tiene que recibir como primer argunemtno una lista
fila.append(3)
fila.append(4)
fila.append(5)
print(fila)  # deque([1, 2, 3, 4, 5])
# para eliminar elementos de la lista como si fuera una lista usamos el metodo popleft
fila.popleft()
print(fila)  # deque([2, 3, 4, 5])
fila.popleft()
fila.popleft()
fila.popleft()
fila.popleft()
if not fila:  # se usa el not porque [] va a detecctar la lista vacia
    # recordar los valores falsy (), 0, none, ""
    print("fila vacia")
