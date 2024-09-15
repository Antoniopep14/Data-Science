mascotas = ["pelusa",
            "jacobo",
            "pulga",
            "wolfgang",
            "jacobo",
            "felipe",
            "chanchito"]
# palabra reservada del
# metodo .insert, .append, .remove, .pop, .clear
# si quiero agregar un elemento a la lista
# para este caso en el indice 1
# lo que tengo que hacer es recorrer la lista y hacer espacio en el indice 1
# para agregar el otro valor
mascotas.insert(1, "melvin")  # donde 1 es el indice donde lo queremos agregar
# ['pelusa', 'melvin', 'jacobo', 'pulga', 'wolfgang', 'jacobo', 'felipe', 'chanchito']
print(mascotas)
mascotas.append("brisa")
# con append agregamos un elemento al final de la lista
# ['pelusa', 'melvin', 'jacobo', 'pulga', 'wolfgang', 'jacobo', 'felipe', 'chanchito', 'brisa']
print(mascotas)
# ahora eliminaremos elementos de un lista
mascotas.remove("jacobo")  # remove solo va a eliminar el primer elemento
# ['pelusa', 'melvin', 'pulga', 'wolfgang', 'jacobo', 'felipe', 'chanchito', 'brisa']
print(mascotas)
# por lo que al tener 2 jacobo aun seguira quedando 1
mascotas.pop()  # esto va a eliminar solo el ultimo elemento de un listado
# ['pelusa', 'melvin', 'pulga', 'wolfgang', 'jacobo', 'felipe', 'chanchito']
print(mascotas)
# pero .pop tambien se puede usar para eliminar un elemento en especifico
# usando el indice a diferencia de remove
mascotas.pop(1)
# ['pelusa', 'pulga', 'wolfgang', 'jacobo', 'felipe', 'chanchito']
print(mascotas)
del mascotas[2]  # tambien nos permite eliminar 1 elemento de 1 arreglo
# al hacer esto uno tras otro, debemos tomar en cuenta que el numero de indice
# va cambiando conforme añadimos o quitamos elementos
# entonces es mejor verificar cada que hacemos un cambio
# donde esta el elemento que queremos quitar actualmente
print(mascotas)  # ['pelusa', 'pulga', 'jacobo', 'felipe', 'chanchito']

# si queremos limpiar una lista usamos lo sig
mascotas.clear()
print(mascotas)
