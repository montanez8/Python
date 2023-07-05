import math as m
'''
Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.
'''

area_circulo = lambda radio : round(m.pi *m.pow(radio, 2),2)
radio = int(input("Digite el radio del circulo: "))
volumen_cilindro = lambda area_circulo , altura :round(area_circulo * altura,2)
altura = int(input("Digite la altura del cilindro: "))

print(f"el area del circulo es {area_circulo(radio)} y el volumen del cilindro es: {volumen_cilindro(area_circulo(radio),altura)}")
