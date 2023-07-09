def leer_string(msg):
	while True:
		try:
			n = input(msg)
			if n.strip() == '':
				print('Error. Ingrese un nombre valido')
				input('Digite cualquier letra para continar ...')
				continue
			return n

		except Exception as e:
			print('!Error! .Al Ingresar el nombre', e.message())


def leer_int(msg):
	while True:
		try:
			n = int(input(msg))
			return n
		except ValueError:
			print('!Error! Ingrese un numero valido')


def pograma_academico():
	while True:
		print('\n******')
		print('Pograma Academico')
		print('******\n')
		print('1.Tecnico en sistemas')
		print('2.Tecnico en desarrolo de videojuegos')
		print('3.Tecnico en animacion digital')
		op = leer_int('\n>> Opcion (1 a 3)?')
		if op < 1 or op > 3:
			continue
		return op

def beca():
	while True:
		print('\n******')
		print('Indicador de beca')
		print('******\n')
		print('1.Beca por rendimiento académico')
		print('2.Beca Cultural Deportes')
		print('3.Sin beca')
		op = leer_int('\n>> Opcion (1 a 3) : ')
		if op < 1 or op > 3:
			continue
		return op

def calcular_matric(pogram_acad, beca):
	if beca == 1:
		des = 50
	elif beca == 2:
		des = 40
	else:
		des = 0

	if pogram_acad == 1:
		valor_matric = 800000

	elif pogram_acad == 2:
		valor_matric = 1000000

	else:
		valor_matric = 1200000

	valor_neto = valor_matric - (valor_matric * des / 100)

	return valor_neto






cod = leer_int('Ingres el codigo del estudiante: ')
nombre = leer_string('Digite el nombre del estudiante: ')
program_acad = pograma_academico()
beca = beca()

valor_pagar = calcular_matric(program_acad, beca)

print(f'El estuduante {nombre} tiene que pagar un valor de matricula de: ${valor_pagar:,}')