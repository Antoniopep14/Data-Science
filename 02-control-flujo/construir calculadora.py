# verificar si hay numero sino solicitar uno
# si hay numero solicitar operacion
# solicitar segundo numero
# mostrar n1 y guardar como primer numero
# empezar de nuevo
print("Bienvenidos a la calculadora")
print("Para salir ecribe salir")
print("Las operaciones son suma, resta, multi, div")

n1 = ""  # siempre definir variables antes de empezar
while True:  # mantiene la ejecucion infinita
    if not n1:  # verifica si n1 tiene valor asignado
        n1 = input("ingresa primer numero: ")
        if n1.lower() == "salir":
            break
        try:
            n1 = int(n1)
        except ValueError:
            print("ingresa un valor valido, si quieres terminar escribe salir")

    operacion = input("ingresa operación: ")
    if operacion.lower() == "salir":
        break

    n2 = input("ingresa segundo numero: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if operacion.lower() == "suma":
        n1 += n2
    elif operacion.lower() == "resta":
        n1 -= n2
    elif operacion.lower() == "multi":
        n1 *= n2
    elif operacion.lower() == "div":
        n1 /= n2
    else:
        print("Operación no válida")
        break

    print(f"el resultado es {n1}")  # una vez que se imprimer esto
    # regresamos al principio del loop
