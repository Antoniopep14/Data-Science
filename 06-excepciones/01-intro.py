# vamos a ver los errores de anera que el cliente final no pueda verlos
# sino que seamos nosotros quienes los veamos para despues arreglarlos
# try:  # va a permitir avanzar al programa
# n1 = int(input("Ingresa primer número: "))
# except:  # va a arrojar lo que le digamos en caso de que lo de arriba marque error
# por ejemplo usar un str en lugar de un int
# print("Ingresa un numero")

# comentamos el codigo de arriba y agregamos un bucle while
while True:
    try:
        n1 = int(input("Ingresa primer número: "))
        break  # Sale del bucle si se ingresa un número entero válido
    except:
        print("Ingresa un número válido")
