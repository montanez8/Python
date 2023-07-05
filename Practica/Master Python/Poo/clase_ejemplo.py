class Taza():
    color = "Blanco"
    mensaje = None
    material = "Porcelana"
    limpia = True


# Instanciar una clase
taza = Taza()
# cambiar atributo de una clase
taza.color = "Verde"
# print(taza.color)


class vehiculo():
    # atributos de clase
    pais_origen = "Alemania"

    # metodo de instancia  // atrbutos de instancia
    def __init__(self, color, longitud_metros, ruedas):
        self.color = color
        self.longitud_metros = longitud_metros
        self.ruedas = ruedas

    # metodos
    def arrancar(self):
        print("El vehiculo ha arrancado.")

    def detener(setf):
        print("El vehiculo esta detenido.")

    def mostar(setf):
        print(
            f"El vehiculo de color {setf.color} tiene una longitud de {setf.longitud_metros} y {setf.ruedas} ruedas y su pais de origen es {setf.pais_origen}")


vehiculo_1 = vehiculo("blanco", 4, 4)
vehiculo_2 = vehiculo("rojo", 8, 8)
# llamadas a los metodos
vehiculo_1.arrancar()
vehiculo_1.detener()

# crearle un atributo especifico a una instancia
vehiculo_2.aleron = "Fibra de carbono"


vehiculo_2.mostar()