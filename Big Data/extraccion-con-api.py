#acceder a datos de red social y contar los likes
#para importar facebook ejecutar primero
#pip install facebook-sdk

import facebook
import requests 
 
#insertar la api generada aqui
token = "******" 
graph = facebook.GraphAPI(token) 
cantidadComentarios = 100 
PageId = '1415691342026378' 
 
cuentaLikes = 0 
cuetaPaginas = 0 
cuentaComentarios = 0 
ListaComents = [] 
 
bandera = False 
 
coments = graph.get_connections(PageId, 'feed') 
 
print(coments) 
while True: 
    try: 
        for coment in coments['data']: 
            lstComent = [] 
            try: 
                mensaje = coment['message'] 
            except KeyError : 
                continue 
            print(mensaje) 
            lstComent.append(mensaje) 
            lstComent.append(cuentaLikes) 
            ListaComents.append(lstComent) 
            cuentaComentarios  = cuentaComentarios + 1 
            print("") 
            if (cuentaComentarios >= cantidadComentarios): 
                bandera = True 
                break 
        if (bandera): 
            break 
        coments = requests.get(coments['paging']['next']).json() 
    except KeyError : 
                    break 