for j in range(3):  # este se conoce como un outer for/loop
    for k in range(2):  # llamado tambien inner for/loop
        print(f"{j}, {k}")
# esto imprime todas las combinaciones posibles de j y k
# asignandoles numeros desde 0 hasta uno antes del limite que marcamos
# usar un for dentro de un for debe ser una tarea muy selectiva
# siempre hay que tratar de buscar otras alternativas
for j in range(4):
    print(j)
