# un evento es la reaccion del sistema ante un cambio en el estado de alguno de sus elementos
# en el caso de las interfacez el cambio es por la interaccion de los usuarios
from tkinter import *


class interfaz:

    def __init__(self, contenedor):
        self.textoE3 = StringVar()  # declaramos una clase de tipovar

        self.e1 = Label(
            contenedor, text="Convertir Celsius a Farenheit", fg="black")
        self.e2 = Label(contenedor, text="Celsius", fg="black")
        self.e3 = Label(contenedor, text="Farenheit", fg="black")
        self.e4 = Button(contenedor, text="Convertir", fg="black",
                         bg="cyan", command=self.HacerConversion)
        # la ultima instruccion llama a la clase de conversion
        self.e5 = Entry(contenedor, fg="black", bg="white")
        self.e6 = Label(contenedor, text="", fg="black",
                        textvariable=self.textoE3)
        # con la ultima isntruccion podremos modificar la etiqueta de manera dinamica

        # para indicar que este elemento abarcara 2 columnas
        self.e1.grid(column=0, row=0, columnspan=2)
        self.e2.grid(column=0, row=1)
        self.e3.grid(column=0, row=2)
        self.e4.grid(column=0, row=3, columnspan=2)
        self.e5.grid(column=1, row=1)
        self.e6.grid(column=1, row=2)

    def HacerConversion(self):
        # con esta variable obtendremos el valor dentro del campo de texto y lo convertiremos
        cel = float(self.e5.get())
        far = (cel*1.8)+32
        self.textoE3.set(far)


ventana = Tk()
miinterfaz = interfaz(ventana)
ventana.mainloop()
