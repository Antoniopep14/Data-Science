from tkinter import *


class interfaz:

    def __init__(self, contenedor):
        self.e1 = Label(contenedor, text="Etiqueta 1", fg="black", bg="white")
        self.e2 = Label(contenedor, text="Etiqueta 2", fg="black", bg="gray")
        self.e3 = Label(contenedor, text="Etiqueta 3", fg="black", bg="green")

    # ahora agremamos el llamado a pack y agregamos los parametros
        self.e1.pack(side=TOP)  # aparece la etiqueta en medio arriba
        self.e2.pack(side=RIGHT)  # a la derecha
        # abajo con el color relleno hasta donde esta la etiqueta 2
        self.e3.pack(side=BOTTOM, fill=X)


ventana = Tk()
miinterfaz = interfaz(ventana)
ventana.mainloop()
