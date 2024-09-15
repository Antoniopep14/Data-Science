from tkinter import *
# para crear etiquetas necesitamos crear instancias ed la clase label
# requiere 2 parametros principales, el objeto contenedor de la etiqueta y un diccionario


def on_button_click():
    print("Botón clickeado e2")


class Interfaz:
    def __init__(self, contenedor):
        # la etiqueta 1 tendra texto x, letra negra y fondo blanco
        self.e1 = Label(contenedor, text="Etiqueta 1", fg="black", bg="white")
        self.e1.pack()  # se usa para indicar que se agregue el elemento a su contenedor
        # agregue la funcion on button click al boton
        self.e2 = Button(contenedor, text="Mi botón", command=on_button_click)
        self.e2.pack()
# ademas tenemos:
# Checkbutton() despliega una casilla de revision con descripcion
# text = la etiqueta que acompaña la casilla
# Entry() que nos permite ingresar caracteres
# Frame() agrega un subcontenedor o marco al contenedor
# Label() que es la etiqueta de texto fijo
# Listbox()agrega una lista de elementos seleccionables con
# selectmode: tipo de sellcion(browse, single, multiple, extended)
# Radiobutton() agrega una opcion seleccionable con casilla que permite varias opciones
# text= etiqueta mostrada despues del boton

# la sintaxis para crear cualquiera de estos elementos es
# idelemento = clase(contenedor, parametro="valorcadena", parametro="valor numerico"m parametro=variable, ...)


ventana = Tk()  # Objeto de clase tk
miinterfaz = Interfaz(ventana)

ventana.mainloop()  # crea un ciclo inf que permite monitoriar las acciones en la ventana
