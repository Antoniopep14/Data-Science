numero = 1
while numero < 100:  # while es un loop
    # while se usa para seguir con una funcion hasta que se cumpla una carcteristica
    print(numero)
    numero *= 2  # multiplica numero *2 hasta 100
print("2do ejercicio")
comando = ""

while comando != "salir":  # nos va a ejecutar un comando hasta que indiquemos salir
    # si se escribe SALIR, Salir no hsce nada
    # porque un string con mayus es diferente a otro con minus
    comando = input("$ ")
    print(comando)
# para resolver el problea de las mayusculas le agregamos lower a comando
# asi convierte todo a minus
print("ejemplo 3")
comando = ""
while comando.lower() != "salir":
    comando = input("$ ")
    print(comando)

print("ejercicio 4")
# comando = "" para este ejemplo ya no necesitamos la variables definidas de comando

while True:  # esto es un loop infinito
    comando = input("$ ")
    print(comando)
    # la manera de terminarlo seria presionando ctrl + c
    if comando.lower() == "salir":  # de esta manera hacemos que deje de ser infinito
        break
# el problema con los loop infinitos es que pueden ocupar tanta memoria
# que el programa terminaria cerrandose por falta de memoria
