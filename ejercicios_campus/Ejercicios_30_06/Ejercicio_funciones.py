def leer_int(msg):
	while True:
		try:
			n = int(input(msg))
			return n
		except ValueError:
			print('!Error! Ingrese un numero valido')


def cant_string():
	cadena = input('Digite una frase o conjunto de palabras: ')
	cant_palabras = cadena.split()
	print('-' * 40)
	print(f'La cantidad de palabras de la cadena es: {len(cant_palabras)} ')
	print('-' * 40)

def mcd():
	a = leer_int('Ingrese un numero: ')
	b = leer_int('Ingrese un numero: ')
	while b != 0:
		a, b = b, a % b
	print('-'*33)
	print(f'El maximo comun divisor es: {a}')
	print('-' * 33)


def calcular_iva(cantidad, iva=21):
	resultado = (cantidad * iva / 100)
	return resultado + cantidad


def salir():
	print('\nHasta la proxima')
	exit()


def menu():
	print("1- Cantidad de palabras en un String")
	print("2- Calcular el mcd de dos números")
	print("3- Calcular el IVA de una factura")
	print("4- Salir")
	try:
		opcion = int(input("Elige una opción: "))
		return opcion
	except ValueError:
		print("Por favor, introduce un número entero.")


while True:
	opcion = menu()
	if opcion == 1:
		cant_string()
	elif opcion == 2:
		mcd()
	elif opcion == 3:
		cantidad = leer_int('Digite la cantidad sin iva: ')
		res = input(
			'Utilizar el valor del iva por defecto del 21% , Digite (si) o (NO) si va ingresar un valor distinto: ')
		print('-' * 40)
		if res.upper() == 'NO':
			iva = leer_int('Digite el valor de iva a aplicar: ' )
			print('El total de la factura es: ', format(calcular_iva(cantidad, iva), ','))
		else:
			print('El total de la factura es: ', format(calcular_iva(cantidad), ','))
		print('-' * 40)
	elif opcion == 4:
		salir()
	else:
		print("Opción no válida. Por favor, elige una opción del menú.")
