# los diccionarios son unos de los tipos de datos mas utilizados en python
# en conjunto con las listas
# Los diccionarios son una conexion de datos que se encuentran agrupadoss por una llave y un valor
# un diccionario solamete acepta string como la llave
# pero el valor puede ser cualquier tipo de dato
# para abrir y cerrar un diccionario se usan {}
# despues definimos las llaves con un str seguido de : y el dato
punto = {"x": 25, "y": 50}
print(punto)  # {'x': 25, 'y': 50}
# si queremos acceder a un valor de una llave del diccionario usamos su nombre con []
print(punto["x"])  # 25

# podemos agregarle mas llaves al dicionario
# nombreDiccionario[llave] = valor
punto["z"] = 45
print(punto)  # {'x': 25, 'y': 50, 'z': 45}

# ahora vamos a preguntar si "a" se encuentra en el diccionario
if "a" in punto:
    print("encontre a", punto)
else:
    print("no encontre a", punto)

# ahora accederemos a un valor del diccionario
# sin forzar nuestra app-pc
# usaremos el metodo get
print(punto.get("x"))  # 25
print(punto.get("a"))  # none
# si no existe dentro del diccionario nos arroja none
# pero tambien podemos pasarle un valor por defecto en caso de que no exista
print(punto.get("a", 97))

# ahora usaremos el metodo del para eliminar una llave junto a su valor del diccionario
del punto["x"]
print(punto)  # {'y': 50, 'z': 45}

punto["x"] = 45

# puedo usar el metodo for para iterar todas las llaves con su valor
# usando el metodo valor
for valor in punto:
    print(valor)  # esto nos arrojaria z, y, x

# para acceder a los valores debemos hacerlo de la sig manera
for valor in punto:
    print(valor, punto[valor])  # y 50 z 45 x 45

# o de esta manera con el metodo items
# con la dif de que este ootr nos arroja una tupla
for valor in punto.items():
    print(valor)  # ('y', 50) ('z', 45) ('x', 45)

# Y tambien podemos hacer un desempaquetado de las tuplas para acceder a sus valores
# al igual que con las listas
for llave, valor in punto.items():
    print(llave, valor)  # y 50 z 45 x 45

# ahora veamos un uso realista de los diccionarios en python
# para lo cual vamos a crear una lista donde vamos a pasar los dicionarios
# cuando trabajamos con elementos que vienen de una base de datos
# necesariamente vamos a tener que usar un "identificador unico"
# algo asi como el CURP pero aqui se le llama id
usuarios = [
    {"id": 1, "nombre": "pepe"},
    {"id": 2, "nombre": "axel"},
    {"id": 3, "nombre": "anel"},
    {"id": 4, "nombre": "jacqueline"}
]

# si nosotros quisieramos acceder solamente a los nombres de los usuarios
# lo que tendriamos que hacer es iterar los usuarios
for usuario in usuarios:
    print(usuario["nombre"])  # pepe axel anel jacqueline
