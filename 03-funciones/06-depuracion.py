def largo(texto):  # vamos a hacer lo mismo que la funcion len para este ejemplo
    resultado = 0
    for _ in texto:  # aqui deberiamos usar char, pero arroja error
        # asi que lo reemplazamos por un _
        resultado += 1
    return resultado


# el depurador se abre desde el simbolo de play con isecto a la izq
# y se debe marcar un breakpoint, punto rojo a la izq
# para definir donde se va a detener
print("chanchito")
l = largo("Hola Mundo")
print(l)
