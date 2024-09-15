def suma(a, b):
    print(a + b)


suma(2, 5)

#xargs se usan cuando no sabemos el numero de argumentos que vamos a recibir
def suma2(*numeros):  # se uso un nombre x en plural para asignar los parametros
    # el * indica que es algo iterable, es decir que nosotros queremos que sume todos los argumentos de la funcion
    resultado = 0
    for numero in numeros: #numero es palabra guardada
        resultado += numero
    print(resultado)


suma2(2, 5, 7, 23, 4, 3, 54, 10)


def nombre_completo(*nombre):  # se uso un nombre x en plural para asignar los parametros
    # con el * podemos escribir lo que sea dentro de la funcion
    print(*nombre)


nombre_completo("Jose Antonio Garcia Arenas")
