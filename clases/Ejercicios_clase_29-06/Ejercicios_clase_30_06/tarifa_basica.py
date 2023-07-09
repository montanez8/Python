def leer_string(msg):
	while True:
		try:
			n = input(msg)
			if n.strip() == '':
				print('Error. Ingrese un nombre valido')
				input('Digite cualquier lera para continar ...')
				continue
			return n

		except Exception as e:
			print('!Error! .Al ingresar el nombre', e.message())
def leer_int(msg):
	while True:
		try:
			n = int(input(msg))
			if n < 1 or n > 5:
				print('!Error! ingrese un estracto valido (1 a 5)')
				input('Digite cualquier letra para continuar ..')
				continue
			return n
		except ValueError:
			print('!Error! Ingrese un numero entero valido')


def calcular_tarifa_bs(estracto):
	if estracto == 1:
		return 10000
	elif estracto == 2:
		return 15000
	elif estracto == 3:
		return 30000
	elif estracto == 4:
		return 50000
	else:
		return 65000


nombre = leer_string('Ingrese el nombre')
estracto = leer_int('Ingrese el estracto del usuario')

tarifa_bas = calcular_tarifa_bs(estracto)

print(f'''
	El Nombre del usuario: {nombre}
	La tafifa basica es: ${tarifa_bas:,}
	
''')
