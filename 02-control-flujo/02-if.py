n1 = input("ingresa edad")
n1 = int(n1)
edad = n1  # cambiar para obtener otro resultado
if edad > 70:  # todo despues del if debe ir identado
    # para que considere las variables expuestas
    # elif se usa despues del primer if
    print("puedes ver la película con un super descuento")
elif edad > 54:
    print("puedes ver la pelicula con descuento")
elif edad > 17:  # prestar atencion a :
    # que se uso para trabajar sobre if
    # y pone 4 espacios en la siguiente linea
    print("puede ver la película")
    # El orden de if y elif es muy importante
else:  # si if ni elif no se cumple, entonces...
    print("no puedes entrar")
    print("ve a otro lado")


print("listo")
