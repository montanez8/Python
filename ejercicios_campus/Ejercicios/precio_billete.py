'''
Determinar el precio de un billete de ida y vuelta en ferrocarril, conociendo la distancia a recorrer y
sabiendo que si el número de días de estancia es superior a siete y la distancia superior a 800
kilómetros el billete tiene una reducción del 30%. El precio por kilómetros es de 2500 pesos.
'''
distancia = int(input('Ingrese la distancia a recorrer (Km): '))
num_dias = int(input('Ingese el numero de dias de estancia:' ))
precio_km = 2500

if (distancia > 800 and num_dias > 7):
    precio = (distancia * precio_km) * 0.3
    print(f'\n El precio a pagar con el descuento es de {int(precio)}')
else:
    precio = distancia * precio_km
    print(f'\n Precio a pagar sin descuento es: {int(precio)}')
    