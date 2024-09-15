numeros = [1, 2, 3]

# primero = numeros[0] #aqui el 0 = 1, 1=2, 2=3, poruqe la lista tiene los parametros definidos
# segundo = numeros[1]
# tercero = numeros[2]
# de esta forma podemos desempaquetar una lista, pero es una forma fea, horrible de llamarlas
# esto es feo!!

primero, segundo, tercero = numeros
print(primero, segundo, tercero)  # 1 2 3
# para llamar a solo 1 elemento de la lista, se hace de la sig manera
# no necesariamente es primero, le podemos dar el nombre que sea
primero, *otros = numeros  # Al usar el * se toman todos lo elementos dentro de la lista
# y los estamos empaquetando en otros
print(primero)  # da 1
print(primero, otros)  # da 1 [2, 3]

letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
primera, segunda, *otras = letras
print(segunda, otras)  # b ['c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# si le dejamos el * lo desempaqueta todo
print(segunda, *otras)  # b c d e f g h i j
primera, segunda, *otras, ultima = letras
# a b ['c', 'd', 'e', 'f', 'g', 'h', 'i'] j
print(primera, segunda, otras, ultima)
# de esta manera accedimos tambien al ultimo valor de la lista
# a b ['c', 'd', 'e', 'f', 'g', 'h', 'i'] j
