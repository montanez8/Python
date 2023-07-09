class Motocicleta():
    estado = "nueva"
    motor = False

    def __init__(self, color, tipo, capacidad_tanque, matricula, marca, modelo, peso, fecha_fabricacion, velocidad_max, precio):
        self.color = color
        self.tipo = tipo
        self.capacidad_tanque = capacidad_tanque
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.peso = peso
        self.fecha_fabricacion = fecha_fabricacion
        self.velocidad_max = velocidad_max
        self.precio = precio

    def arranccar(self):
        if self.motor == False:
            print("La motocicleta ha arrancado")
            self.motor = True
        else:
            print("La motocicleta ya esta en marcha")

    def detener(self):
        if self.motor == True:
            print("La motocicleta se ha detenido")
            self.motor = False
        else:
            print("La motocicleta No esta en marcha")

    def mostrar_precio(self):
        print(f"El precio de la motocicleta es {self.precio}")


suzuki_gn = Motocicleta("negro", "Cruiser", 12, "NKU23B",
                        "Suzuki", 1998, 130, "12/4/1998", 120, 1500)


suzuki_gn.arranccar()

suzuki_gn.arranccar()

suzuki_gn.detener()
suzuki_gn.detener()

# print(f"El precio de la motocicleta es: {suzuki_gn.precio}")
suzuki_gn.mostrar_precio()
