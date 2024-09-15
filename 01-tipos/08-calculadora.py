n1 = input("ingresa primer numero")  # n1 hace referencia a numero 1
n2 = input("ingresa segundo numero")  # imput pide un dato al usuario

n1 = int(n1)  # se pone esto para que registre los numeros correctamente
n2 = int(n2)  # int transforma el dato en un entero
# int toma los datos ingresados por input
suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2

mensaje = f"""
para los números {n1} y {n2},
el resultado de la suma es {suma}
el resultado de la resta es {resta}
el resultado de la multiplicacion es {multiplicacion}
el resultado de la division es {division}
"""
# f""" arroja el mensaje dentro de las "" al usuario
# dentro de f se usan {} para obtener datos de las variables
print(mensaje)
