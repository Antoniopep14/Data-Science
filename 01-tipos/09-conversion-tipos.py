x = input("")  # Esto siempre va a ser de tipo str

# int() transforma datos en enteros
# str() transforma datos en string
# float() Transforma datos en float
# bool() transforma datos en boolean
# truthy, falsy conceptos en python que evaluan en true o false
# falsy = "" (string vacio), 0, None (1ra mayus)(none es un objeto valuado en falso)
# cualquier otra cosa valua en truthy

print(bool(""))  # false
print(bool("0"))  # true oorque es un str
print(bool(None))  # false
print(bool(" "))  # true porque tiene espacio en el string
print(bool(0))  # false
