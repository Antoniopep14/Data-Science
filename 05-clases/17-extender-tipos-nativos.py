# ahora vamos a extender clases o tipos nativos
# lista = list([1, 2, 3])
# lista.append(4)
# lista.insert(0, 0)
# print(lista) #[0, 1, 2, 3, 4]

# ahora hagamos lo mismo pero de una manera mas intuitiva
class Lista(list):
    def prepend(self, item):  # lo que vamos a hacer con esto es agregar elementos al inicio
        self.insert(0, item)


# y de esta manera estamos extendiendo los tipos nativos de list
lista = Lista([1, 2, 3])
lista.append(4)
lista.prepend(0)
print(lista)  # [0, 1, 2, 3, 4]

# y lo mismo prodriamos hacer con los str, numeros, etc
