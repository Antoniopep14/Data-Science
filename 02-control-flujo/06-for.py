# se usa para muchas cosas
# principalmente se usa a iterar una lista de elementos
# para buscar elementos
# realizar operaciones matematicas
# siempre que programes lo vas a usar
# for es un loop
for numero in range(5):  # notese que la palabra numero indica numeros como tal
    # range es un iterable, otro seria listas, tuplas
    print(numero)  # imprime numeros 0 1 2 3 4
    print(numero, numero * 2)  # da 0 2 4 6 8

buscar = 3
for numero in range(5):
    print(numero)  # imprime los numeros hasta encontra el que le indicamos
    if numero == buscar:
        print("encontrado", buscar)
        break  # Se usa para detener la ejecucion del codigo una vez que encuentra lo que buscamos
else:  # usado para acompañar a for como termino for-else
    print("no encontre el numero buscado")
# si ponemos # al break la funcion sigue y al final muestra el mensaje de ariba

for char in "ultimate python":  # char es caracter
    print(char)
# esta accion va a imprimir los caracteres de ultimate python uno abajo de otro

# for usuario in usuarios:
    # usuario.id
    # de esta forma podriamos buscar usuario
