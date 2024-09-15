# Se caracterizan por ser LiFo
# es decir last in first out, que es lo contrario a las filas
# un ejemplo practivo de esto es cuando presionamos el boton regresar en el historial de navegacion o cuando estamos haciendo codigo
pila = []
pila.append(1)
pila.append(2)
pila.append(3)
print(pila)  # [1, 2, 3]
ultimoElemento = pila.pop()
# Al hacer esto estamos extrayendo el ultimo elemento de la pila y asignandolo a una nueva variable
# otra forma de extraer el ultimo elemento de la lista es usando
print(pila[-1])  # 2 por que el pop de arriba quito el 3
# pero al mismo tiempo estamos extrayendolo de la pila
print(ultimoElemento)  # 3 que fue el elemento  ue quito el pop de arriba
print(pila)
# al final es una lista pero lo estamos trabajando de una manera logica para que funcione como una pila
# ahora revisemos si la pila esta vacia
pila.pop()
pila.pop()  # comentar para otro resultado abajo
if not pila:
    print("pila vacia")
else:
    print("si")
