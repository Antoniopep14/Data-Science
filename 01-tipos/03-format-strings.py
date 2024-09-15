nombre = "Antonio"
apellido = "Arenas"
nombre_Completo = nombre + " " + apellido
# las " " se agregan para tener espacio entre las 2 variables
nombre_completo = f"{nombre} {apellido}"
# f puede ser F se usa para hacer la concadenacion
print(nombre_completo, nombre_Completo)
# el operador de concadenacion es +
# {}: Sirven para definir bloques de código dentro de las clases y métodos.
# siempre que se usen {} dentro de un
# operador de formateo de string (f)
nombrE_completo = f"{nombre[0:2]} {2 + 3}"
print(nombrE_completo)  # An 5
# podemos colocar cualquier expresion dentro del operador f
