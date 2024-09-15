# para definir un string se usan "" o ''
# triple "" se usa para un texto de varias lineas en el string
# o para definir ciertas lineas de codigo

nombre_curso = "Ultimate python"
descripcion_curso = """
Ultimate python,
este curso comtempla todos los detalles
que necesitas aprender para encontrar
un trabajo como programador.
"""
print(nombre_curso, descripcion_curso)
len(nombre_curso)  # da la longitud de un string
print(len(nombre_curso))  # doble parentesis ejecuta las 2 funciones, 15
print(nombre_curso[0])  # [] imprime el primer caracter, U
print(nombre_curso[0:8])  # imprime del primero al 8vo, Ultimate
print(nombre_curso[9:])  # imp del 9 hasta el final, python
print(nombre_curso[:8])  # imp del principio al fin, Ultimate
# [] se usan en operaciones con vectores
# {}: Sirven para definir bloques de código dentro de las clases y métodos.
