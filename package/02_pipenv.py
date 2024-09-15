#esta herramienta combina las 2 anteriores
#escribimos en la terminal pip install pipenv
#para continuar eliminamos la carpeta ENV creada anteriormente
# e instalamos requests usando el comando pipenv install requests

#pipenv nos creo una nueva carpeta para nuestro ambiente virtual
#pero no la agrego a la carpeta de nuestro proyecto
#para poder ver donde se encuentra ejecutamos: pipenv --venv
#Este comando te mostrará la ruta al directorio del entorno virtual actual. 
#Si muestra una ruta diferente o si no muestra ninguna, significa que no tienes un entorno virtual activo.

#al crearnos el entorno virtual podemos cambiarnos a el desde la parte inferior derecha
#donde tenemos la version de python en la que estamos trabajando
#tambien si eliminaramos request de manera global, prodriamos seguir usandola
#en nuestro entorno virtual porque on le afecta

#para ejecutar un script usando el ambiente virtual
#usamos el siguiente comando: pipenv shell
#para salir: exit

#para obtener la ruta donde estamos trabajando:
# pipenv --venv
#para eliminar algo desde la terminal se usa 
#rm -rf direccion obtenida con

#si hubiesemos eliminado esa ruta podriamos instalar los mismo paquetes
#desde el archivo pipfile.lock que se nos creo anteriormente
#para lo cual debemos ejecutar:
    # pipenv install --ignore-pipfile
#de otra manera seria: *pero podria darnos errores por el tipo de version
    #pipenv install

#ADMINISTRAR DEPENDENCIAS
#al ejecutar: pipenv graph
#nos va a mostraar todas las dependencias de nuestro proyecto y sus subdependencias
#cuando eliminamos la dependencia de request esas subdependencias siguen quedandose
#porque pipenv no sabe si estas podrian estar siendo utilizadas por otra dependencia
#sin embargo no quedan en el registro de pipfile por lo que al ejecutar un pipenv install
#otro desarrollador no tendria esas subdependencias automaticamente

#para ver paquetes que pueden  ser acutalizados a otra version, ejecutamos:
# pipenv update --outdated
#esto nos va a mostrar la evrsion mas actual de acda paquete
#y podemos modificarla en el archivo pipfile de la siguiente manera:
#en la seccion de [packages] en la dependecia deseada: requests = "==2.*"
#donde decimos que no queremos una version mas alla de la 2. pero si la mas reciente
#ahora ejecutamos: pipenv update
#si queremos actualizar solo un paquete seria: pipenv update requests




