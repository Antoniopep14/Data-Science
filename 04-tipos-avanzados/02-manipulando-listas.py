# podemos acceder a cualquier valor de la lista
mascotas = ["wolfgang", "pelusa", "pulga", "copito"]
# aqui debemos especificar el valor al que quieremos acceder
print(mascotas[0])  # nombre de lista seguido del valor que queremos
# contando desde 0 hasta el numero del valor que queremos
# Esto cambia el elemento de la lista por otro que le decimos
mascotas[0] = "Bicho"
print(mascotas)
# da ['Bicho', 'pelusa', 'pulga', 'copito']
print(mascotas[:3])  # tambien podemos escoger de donde a donde debe tomar
# da ['Bicho', 'pelusa', 'pulga']
# notese que el primer valor de la lista sigue cambiado
print(mascotas[-2])
# si usamos un valor negativo cuenta del final a la izquierda
print(mascotas[::2])
# al hacer esto le estamos diciendo
# que tome el primer elemento, el sig lo salta
# el sig lo toma, el sig lo salta, etc...
print(mascotas[1::2])
# Es lo mismo de arriba pero ahora va a empezar desde el indice 1
# El de en medio indica hasta que indice queremos llegar
print(mascotas[1:2:2])

numeros = list(range(21))
print(numeros[::2])  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(numeros[1::2])  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(numeros[3:11:2])
# [3, 5, 7, 9] el 11 no lo tomo porque realmente llego hasta el 10
