def no_space(texto):
    nuevo_texto = ""  # string vacio
    for char in texto:
        if char != " ":  # si caracter es diferente a espacio
            nuevo_texto += char  # nuevo texto=nuevo texto + caracter
    return nuevo_texto  # para llamar a la funcion de vuelta

# otra forma mas elegante de hacerlo


def reverse(texto):
    texto_al_reves = ""  # string vacio
    for char in texto:  # para caracter en texto
        # esto se encarga de concadenar los caracteres invertidos
        # esto lo que hace es validar letra por letra
        texto_al_reves = char + texto_al_reves
        # empezando para hola por la "h" y poniendola en la variable texto al reves
        # depues le suma la "o" al texto y queda oh
        # despues le agrega la l y queda loh y asi sucesivamente
    return texto_al_reves

# palindromo es una palabra o frase escrita igual al derecho y al reves como reconocer


def es_palindromo(texto):
    # ahora tenemos que definir la funcion no space
    texto = no_space(texto)
    # para usarla dentro de la funcion
    # se hace pirmero esta pra quitarle los espacios al texto
    texto_volteado = reverse(texto)  # lo mismo con la funcion reverse
    # ahora obtenemos el segundo valor y podemos usarlo para comparar
    return texto.lower() == texto_volteado.lower()


print(es_palindromo("Abba"))  # los primeros 3 deben dar true
print(es_palindromo("reconocer"))
print(es_palindromo("amo la paloma"))
print(es_palindromo("anel"))  # debe dar false
# aqui agregamos la frase al inicio para que despues agregue el resultado de la funcion
print("somos o no somos", es_palindromo("somos o no somos"))
# dando= somos o no somos True
