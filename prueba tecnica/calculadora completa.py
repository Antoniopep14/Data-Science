
resultado = ""
print("Bienvenido a la calculadora")
print("Las operaciones son suma, resta multi y div")
print("si deseas salir escribe salir")

while True:
    if not resultado:
        while resultado != int:
            resultado = input("ingresa el primer número: ")
            resultado = resultado.lower()
            if resultado == "salir":
                break
            elif resultado != "salir":
                try:
                    resultado = int(resultado)
                    break
                except ValueError:
                    print("ingresa un número valido")
    if resultado == "salir":
        break

    n2 = input("ingresa segundo número: ")
    n2 = n2.lower()
    if n2.lower() == "salir":
        break
    while not n2 == int:
        try:
            n2 = int(n2)
            break
        except ValueError:
            print("ingresa un número válido")
            n2 = input("ingresa el segundo número")
    if n2 == "salir":
        break

    print("Las operaciones son suma, resta, multi y div")

    while True:
        operacion = input("ingresa una operación: ")
        operacion = operacion.lower()
        if operacion == "salir":
            break
        if operacion == "suma":
            resultado = resultado + n2
            print(f"el resultado de la {operacion} es: {resultado}")
            break
        if operacion == "resta":
            resultado = resultado - n2
            print(f"el resultado de la {operacion} es: {resultado}")
            break
        if operacion == "multi":
            resultado = resultado * n2
            print(f"el resultado de la multiplicación es: {resultado}")
            break
        if operacion == "div":
            resultado = resultado / n2
            print(f"el resultado de la división es: {resultado}")
            break
        else:
            print("Ingresa una operación valida")
            continue
    if operacion == "salir":
        break
