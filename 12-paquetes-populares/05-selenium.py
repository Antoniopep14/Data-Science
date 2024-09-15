from selenium import webdriver
##para encontrar obejtos en la web vamos a apoyarnos de otro modulo de selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#nos va a ayudar a crear una instancia que nos ayudara a manipular el explorador web
##tenemos que crear una variable que mantenga chrome abierto si asi lo requerimos
##ya que al ejecutar el codigo sin la sig variable el explorador solo se abre y cierra
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options)
##aqui agregamos el timepo de espera del que hablamos mas abajo
browser.implicitly_wait(3)#se pone el timepo en segundos
#ahora tenemos que indicarle a chrome que es lo que queremos que haga
#con el metodo de get nosotros le podemos indicar que queremos que visite
browser.get("https://github.com")
#a continuacion le vamos a indicar que es lo que queremos que haga
#los pasos van a ser, que pinche en el boton de iniciar sesion, luego que rellene los campos y logee
#una vez dentro va a validar que se encuentre mi nombre de ussuario en una seccion especifica de la web
link = browser.find_element(By.LINK_TEXT, "Sign in")
link.click()
#hay pagians web que cargan el tipo de contenido que necesitamos despues de cargar todo el html
#para ello tenemos que indicarle a selenium que espere cierto tiempo antes de buscar el contenido
#para evitar que nos arroje errores por la falta de el mismo

user_input = browser.find_element(By.ID, "login_field")
pass_input = browser.find_element(By.ID, "password")

user_input.send_keys("Antoniopep14")
pass_input.send_keys("Pp142103.")
#ahora tenemos que hacer que presione enter despues de escribir eso
#para lo cual importaremos la libreria de keys para usar las teclas
pass_input.send_keys(Keys.RETURN)
#ahora validempos si dentro de algun elemento html existe mi nobre de usuario
profile = browser.find_element(
    By.CLASS_NAME, 
    "color-fg-default.lh-0.mb-2.markdown-title")#las clases venian de la inspeccion en la web de la sig manera:
#color-fg-default lh-0 mb-2 markdown-title
#asi que las pegamos y ponemos un . entre ellas

label = profile.get_attribute("innerHTML")
#print(label)#Antoniopep14<span class="color-fg-muted">/</span>Zelda
#ahora si comprobemos si se encuentra mi usuario
assert "Antoniopep14" in label#y como no indica error sabemos que se encuentra

#ahora solo necesitamos cerrar el explorador al terminar el requesr
browser.quit()