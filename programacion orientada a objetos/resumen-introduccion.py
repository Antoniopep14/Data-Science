# aceeder a un elemento dentro de una lista usando el indice, pero que esta dentro de otro indice se hace de la sgi forma
lista = ["perro", "gato", ["iguana", "cocodrilo", "ave"]]
lista2 = lista[2][0]
print(lista2)  # iguana

# un diccionario puede contener, valores, str, listas, etc
# y tambien podemos acceder a un elemento del diccionario, aun si este se encuentra en una lista
dic = {"clave1": "Bipedo",
       "clave2": 6,
       "clave3": ["caminar", "correr", "saltar"]}

dic2 = dic["clave3"][1]
print(dic2)  # correr

# dentro de las clases caracteristicas se defimem en __init__
# tambien aqui se pueden poner variables de instancia


class Persona:
    def __init__(self, edad, nombre):
        self.edad = edad
        self.nombre = nombre
        print("Se ha creado a", self.nombre, "de", self.edad)

    def hablar(self, palabras="No sé que decir"):
        print(self.nombre, ": ", palabras)

# una clase que tiene herencia o subclase


class Deportista(Persona):
    # tambien se puede sobreescribir el metodo constructor de la clase que hereda
    # y usar solo el metodo hablar por ejemplo de la clase persona
    # def __init__(self, edad, nombre, deporte):
    #     self.edad = edad
    #     self.nombre = nombre
    #     self.deporte = deporte

    def practicarDeporte(self):
        print(self.nombre, "voy a practicar")

# para trabajar metodos con tuplas se usa * y para diccionarios **
# para encapsular un atributo o metodo de una clase se usa __ antes de la palabra
# para acceder a un metodo encapsulado, tendraimos que meterlo dentro de una funcion propia de la clase que de return a el


juan = Persona(18, "Pepe")  # Se ha creado a Pepe de 18
juan.hablar()  # Pepe :  No sé que decir
juan.hablar("Hola, estoy hablando")  # Pepe :  Hola, estoy hablando
# ahora llamemos a la subclase, que herede los metodos de otra clase
anel = Deportista(18, "Anel")  # Se ha creado a Anel de 18
anel.practicarDeporte()  # Anel voy a practicar

i = 0
while i <= 10:
    tabla = 7*i
    print("7 X", i, "=", tabla)
    i = i+1

for j in range(0, 11):
    print("7 X", j, "=", j*7)
    j = j+1

# METODOS DE CADENAS
# .count = cuenta las veces que se repite un caracter o cadena x en el rango de inicio a fin
# .replace("x", "y", nunmero) = reemplaza los valores de x por y de acuerdo al numero de veces que se especifique
# .split("x", numero) = busca el caracteer x, los quita y organiza nuevas subcadenas, el numero se puede usar para indicar las veces que queremos reemplazar x
# .find y .rfind = buscan un caracter y regresa el indice donde se encuentra, ya sea de izq a der o de der a izq
# .join("x") = junta los elementos de una tupla o lista con el elemento x
# str = ("a", "b") \n v = "-" \n ptint v.join(str) \n a-b

# METODOS DE LISTAS
# .index(x) = busca el indice de x en una lista, si no se encuentra marca error
# .append(x) = agrega el elemento al final de la lista
# .count(x) = cuenta el numero de veces que aparece x
# .insert(indice, x) = inserta el valor de x en el indice y recorre los demas valores de la lista
# .extend(x) = agrega una nueva tupla, cadena o lista a otra lista
# .pop(indice) = elimina el valor de la lista de acuerdo al indice
# .remove(x) = elimina el primer valor de x en la lista
# .reverse() = invierte el orden de los valores de la lista

# ERRORES
SyntaxError

# refactorizar: mejorar estructura
# da mantenimiento
# facilita adicion de codigo redundancias
# reduce el tiempo de procesamieto y uso de meoria
# refactor
# hacer lista de cambios

# documentacion. explica cada parte del programa
# doctrings: cadena de carac entre """describe
# que hace el codigo """
# comentarios: #para describir como se hacen los procesos
# estos se usan para proposito, la version o si es respaldo, nombre tambien

# etapas del desarrollo de sofware: plneacion, codificacion pruebas y documentacion, implementacion y mantenimiento
# programador web: backend(parte funcional), frontend(diseño grafico)
# programador de apps, software, videojuegos


# atencion al usuario
# identifica expectativas, escucha necesidaeds, coparte consejos, anticipa dudas, contesta
# estrategias: responsabilidades monitores y sokucion
# protocolo
# preguntas frecuentes

# profesionalizacion: anticipar errores, 
# analizar probleamas, documentacion, 
# tomar cursos, realizar presentaciones,
# retroalimentacion, actualizacion

# como cobrar: para quien trabajas, actividades, personal
# pueder ser por: horas de trabajo, tiempo de entrega
# ajustes: 2 cambios gratis, el extra con 5% extra