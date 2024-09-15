animal = "Elefante"
print(animal.upper())  # todos estos son metodos
# que son funciones dentro de un objeto
# upper convierte todas la letras en MAYUS
print(animal.lower())  # letras a minus
print(animal.capitalize())
# 1er caracter del string en MAYUS y el resto en minus
print(animal.title())  # 1er caracter de cada palabra en MAYUS y el resto en minus
# remueve espacios a la der e izq de los "", tambien da error a los booleans
print(animal.strip())
print(animal.upper().strip())  # se pueden combinar funcones
print(animal.find("fa"))  # encuentra el indice con esa cadena de caracteres
# el resultado seria 3
# si no existe arroja -1
# remmplaza la cadena de caracteres que digamos
print(animal.replace("fa", "j"))
print("fan" in animal)  # Dice si se encuentra la cadena en la variable
print("fan" not in animal)  # dice si no se encuentra
# las ultimas 2 devuelven un boolean
