from pathlib import Path

path = Path("rutas-08")
# las formas de trabajar con directorio son:
# path.exists()#si existe
# path.mkdir()#make dir.. crea el directorio
# path.rmdir()#remove dir... eliminan el directorio con condicion
# solo si no hay ningun archivo dentro de este es decir que este vacio
# path.rename("chanchito_feliz")#para cambiar nombre al directorio
# print(path.iterdir())#Esto nos devuelve un objeto generador, que podemos iterar
# <bound method Path.iterdir of WindowsPath('rutas-08')>
for p in path.iterdir():
    # FileNotFoundError: [WinError 3] El sistema no puede encontrar la ruta especificada: 'rutas-08'
    print(p)
    # esto lo hace porque no estamos en la carpeta correcta, lo que debemos hacer es movernos con la terminal
    # escribiendo cd ..(para ir hacia atras) o cd + nombre del direcctorio para avanzar
    # cd..  ,   cd curso-py  ,  poe ejem
# estando en la carpeta correcta nos itera el contenido de la ruta
# rutas-08\01-path.py
# rutas-08\02-directorios.py
# rutas-08\03-inyeccion-deps.py
# rutas-08\dos
# rutas-08\uno
# rutas-08\__pycache__
# tambien podemos crear listas filtrando dir y dejando archivos por ejem
archivos = [p for p in path.iterdir() if not p.is_dir()]
print(archivos)
# [WindowsPath('rutas-08/01-path.py'), WindowsPath('rutas-08/02-directorios.py'), WindowsPath('rutas-08/03-inyeccion-deps.py')]
#en mac va a salir PosixPath
#METODO GLOB
# pero si queremos filtrar archivos por su nombre o extension debemos usar otro metodo
# *.py para buscar extension por ejemplo donde * es lo que sea antes de py
# o tambien buscar "01-*.py" para buscar achivos .py con 01- al inicio
archivos2 = [p for p in path.glob("*directorios*")]
print(archivos2)  # [WindowsPath('rutas-08/02-directorios.py')]
# ahora queremos todos los archivos.py de todas las carpetas dentro de rutas
archivos3 = [p for p in path.glob("**/*.py")]#aqui si usamos / ya seea en windows o mac
#lo mismo de arriba podriamos hacerlo directamente con el metodo rglob
# archivos3 = [p for p in path.rglob("*.py")]
print(archivos3)
#[WindowsPath('rutas-08/01-path.py'), WindowsPath('rutas-08/02-directorios.py'), WindowsPath('rutas-08/03-inyeccion-deps.py'), WindowsPath('rutas-08/dos/__init__.py'), WindowsPath('rutas-08/uno/__init__.py')] 

