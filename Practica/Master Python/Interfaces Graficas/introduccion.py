# modulo para graficar interfaces 
# import tkinter
from tkinter import *
# variable que almacena la ventana
root = Tk()
# titulo de la ventana
root.title("Pychardiando")

# tamaño de la ventana y posicion de la ventana (ancho-alto-x-y)
root.geometry("800x600+560+220") 
#  creacion de una etiqueta
mensaje = Label(root , text="Pychardiando")
mensaje2 = Label(root , text="Hola mundo").grid(row=0 , column= 0)
# mostar etiqueta
# mensaje.pack()
# mensaje2.pack()
# grid()
mensaje.grid(row=1 , column=0)
#  Bucle de ejecución permite mantenar la ventana en ejecucion
root.mainloop()

