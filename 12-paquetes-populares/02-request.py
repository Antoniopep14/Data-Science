#una api rest es el formato mas comun con el cual nosotros podemos trbajar en internet
#para obtener datos de una aplicacion o enviarle datos
#supongamos que r+queremos conectarnos con otra aplicacion
#y la api es la siguiente
"https://api.holamundo.io/users/"
#si fuera una api real nos entregarioa una lista con diccionarios, y cada diccionario contendria un usuario
#a eso se le conoce como api rest: application programming interface representational state transfer
#para usar la aip necesitaremos varios verbos:
    # GET: listar
    # Post: crear
    # Put/Patch: actualizar
    # DELETE: eliminar

#para ver un ejemplo practivo usamos chrome y escribimos json typicode
#y en resources abrimos el de 10 users

import requests
url = "https://jsonplaceholder.typicode.com/users"
r = requests.get(url, timeout=10)

# print(r) #<Response [200]>
# print(r.status_code, r.text)#200 mas el texto del dicc
#pero yo no necesito el estado, o el texto, yo necesito que me de la lista
#para eso usamos el metodo json
r = r.json()
for user in r:
    print(user["name"])# de eta manera estamos obteniendo el nombre de cada usuario en la lista

#para poder obtener un usuario en particular
url2 = "https://jsonplaceholder.typicode.com/users/1"
#donde el numero 1 es el numero de id del usuario al que queremos acceder
r2 = requests.get(url2, timeout=10)
r2 = r2.json()
print(r2)

#ahora vamos a ver como crear un recurso
url3 = "https://jsonplaceholder.typicode.com/users"
#cuando nosotros creamos un post, debemos especificar los datos que vamos a mandar
user3 = {
    "id": 11,
    "name": "Chanchito feliz"
}
r3 = requests.post(url3, timeout=10, data=user3)
print(r3.status_code)#201 lo que indica que se crearia

#para actualizar usando put/patch si deberiamos de especificar el numero 
url4 = "https://jsonplaceholder.typicode.com/users/2"
user4 = {
    "name": "Chanchito feliz"
}
r4 = requests.put(url4, timeout=10, data=user4)
print(r4.status_code)#200 que indica ok


url5 = "https://jsonplaceholder.typicode.com/users/2"
r5 = requests.delete(url5, timeout=10)
print(r5.status_code)#200 que indica ok

#cuando una api protegida y que requiere de una autorizacion 
# para ser usada haremos el uso de headers
url6 = "https://jsonplaceholder.typicode.com/users/2"
apikey6 = "123456"
headers = {
    "Authorization": f"Bearer {apikey6}"
}
r6 = requests.delete(url6, timeout=10, headers=headers)
print(r6.status_code)

#para el 95% de los casos tendremos que hacer uso de estas cabeceras
#la api te da el formato necesario para acceder a ella, tambien podria ser
#headers = {"Authorization": apikey}
#headers = {"x-key": f"Bearer {apikey6}"}