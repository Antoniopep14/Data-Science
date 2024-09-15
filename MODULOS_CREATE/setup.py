import setuptools
from pathlib import Path

long_desc = Path("README.md").read_text()

setuptools.setup( 
    name="holamundoplayer",#nombre del paquete en la carpeta
    version="0.0.1",
    long_description=long_desc,
    packages=setuptools.find_packages(
        exclude=["mocks", "tests"]
    )
)

#ejecutamos: python setup.py sdist bdist_wheel
#sdist significa source distribution
#bdist significa build distribution
#para cargar el modulo una vez generados los build y dist
#ejecutamos: twine upload dist/*
#ingresamos usuario y contraseña de pypin
#Freky14 Pp142103.
#de esa manera podemos crear, subir e instalar nuestros propios paquetes
