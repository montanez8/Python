def leer_int():
	while True:
		try:
			n = int(input('Ingrese un numero entero: '))
			return n
		except ValueError:
			print('!Error! Ingrese un numero valido')


def suma(a, b):
	result = a + b
	return result


# Ejemplo de uso de la función

a = leer_int()
b = leer_int()

print('El resultado de la suma es:',suma(a, b))
