#no todas la web tiene una api o servicio al cual podamos acceder directamente
#tomemos de ejemplo https://stackoverflow.com/questions
#desde la cual obtendremos los nombres de las preguntas mas recientes y de los usuarios que las realizan
#ahora instalamos una herramienta que nos va a ayudar a analizar los sitios web
# pipenv install beautifulsoup4
import requests
from bs4 import BeautifulSoup
#beautifulsoup no es para navegar, ko que hace es recibir un str html
#request va a ser la encargada de buscar y extraer los datos de la web
url = "https://stackoverflow.com/questions"
respuesta = requests.get(url)
texto = respuesta.text
soup = BeautifulSoup(texto, "html.parser")
#despues de la variable tenemos que indicarle el interprete que va a usar
#con respecto a lo que le estamos pasando, ya que beautifulsoup puede interpretear muchos tipos de datos
#por ejemplo xml
#despues usaremos el metodo de select de soup que nos va a permitir seleccionar
#elementos html ya sea por su id usando ! o por su clase utiliando el .
#esto ultimo son selectores, estaria bien ver un curso sobre html y css
#a grandes rasgos al darle inspeccionar a la pagina podemos ver los datos de interes para nosotros
#las preguntas tienen un id diferente pero comparten una clase
#por lo que usaremos la clase para este select y trabajaremos con .
preguntas = soup.select(".s-post-summary")
#print(preguntas[0])#esto nos arrojaria todo el contenido html de la primer pregunta
#este metodo de select me devuelve un listado
#por lo tanto yo sé que lo puedo iterar
for pregunta in preguntas:
    titulo = pregunta.select_one(".s-link").get_text()
    #usamos select_one para indicar que solo queremos 1 elemento
    #que seria el de la etiqueta s-link
    #print(titulo)
    #y esto nos daria los titulos de las preguntas que este encontro
    
    #ahora obtengamos el nombre de los usuarios
    usuario = pregunta.select_one(".s-user-card--link").get_text()
    print (f"{usuario}Titulo: {titulo}")



