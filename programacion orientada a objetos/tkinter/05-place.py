from tkinter import *
# el adiministrador place, sirve para colocar los elementos en una posicion especifica


class interfaz:

    def __init__(self, contenedor):
        self.e1 = Label(contenedor, text="Etiqueta 1", fg="black", bg="white")

        # estas son las coordenadas definidas en pixeles
        self.e1.place(x=20, y=30, width=120, height=25)
        # y define el ancho y alto de la etiqueta


ventana = Tk()
miinterfaz = interfaz(ventana)
ventana.mainloop()
