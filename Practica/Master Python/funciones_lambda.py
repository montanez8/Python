import math as m
# solo puede tener una expresion
# se guarda en una variable para poderla invocar o llamar
multiplicacion = lambda a, b : a * b


print(multiplicacion(3, 6))

# declaracion y llamada en una sola linea

(lambda num1, num2: print(num1 * num2))(3, 67)


# ercicios 

area_circulo = lambda radio : m.pi * (radio ** 2)
radio = float(input("Digite el radio del circulo:\n"))
print(f"El area del circulo es: {round(area_circulo(radio))}")


colores = ["rojo","azul","verde","amarillo"]

(lambda color : print(f"El color {color} se encientra en la posicion {colores.index(color)} de la lista colores"))("azul")
