#para importar una biblioteca podemos presionar ctrl + . sobre los metodos de la biblioteca
#en caso de haberlos usado mas adelante sin importarlos
import os
from pathlib import Path
import sys
print(sys.argv)
#ahora abrimos la terminal y escribimos python 11-modulos-nativos/05-cli.py
#esto nos da un listado donde el primer elemento es nuestro archivo
# ['11-modulos-nativos/05-cli.py']
#le podemos pasar valores escribiendo
# python 11-modulos-nativos/05-cli.py mas valores que queremos
#['11-modulos-nativos/05-cli.py', 'mas', 'valores', 'que', 'queremos']

#ya que sabemos esto crearemos una app que renombre nuestro archivo
def cli(args):
    #primero validamos si el scrip tiene mas de 1 de longitud
    if len(args) == 1:
        print("no se pasaron argumentos")
        return
    #ahora preguntaremos si tiene 3 elementos 
    # que son el archivo, archivo de origen y archivo de destino
    if len (args) != 3:
        print("se necesitan 2 argumentos")
        return
    origen = args[1]
    o = Path(origen)
    if not o.exists():
        print("origen no existe")
        return
    
    destino = args[2]
    d = Path(destino)
    if d.exists():
        print("el destino no puede existir")
        return

    os.rename(str(origen), str(destino))
    print("Archivo renombrado con exito")

cli(sys.argv)
#rcreamos un archivo en modulos

#ahora ejecutamos escribiendo en la consola, para que funcione necesita:
# python 11-modulos-nativos/05-cli.py 11-modulos-nativos/lala 11-modulos-nativos/lala-destino.md
#nos dice
# ['11-modulos-nativos/05-cli.py', '11-modulos-nativos/lala', '11-modulos-nativos/lala-destino.md']
# Archivo renombrado con exito
#y lala ahora es lala-destino.md