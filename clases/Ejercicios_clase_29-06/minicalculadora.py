def leer_int(msg):
	while True:
		try:
			n = int(input('Ingrese un numero entero: '))
			return n
		except ValueError:
			print('!Error! Ingrese un numero valido')
def ms_error(msg):
	print('--> !Error!',msg)
def menu():
	while True:
		print('\n******')
		print('Menu')
		print('******\n')
		print('1.Sumar')
		print('2.Restar')
		print('3.Multiplicar')
		print('4.Dividir')
		print('5.Potencia')
		print('6.Factoria')
		print('7.Salir')
		op = leer_int('\n>> Opcion (1 a 7)?')
		if op < 1 or op > 7:
			ms_error('Opcion no valida')
			continue
		return op
def sumar():
	print('*'*4 ,'Sumar','*'*4)
	a = leer_int('Ingrese el primer numero')
	b = leer_int('Ingrese el segundo numero')
	print(f'La El resultado de la suma es: {a + b}')

def restar():
	print('*' * 4, 'Restar', '*' * 4)
	a = leer_int('Ingrese el primer numero')
	b = leer_int('Ingrese el segundo numero')
	print(f'La El resultado de la Resta es: {a - b}')
def multiplicar():
	print('*' * 4, 'Multiplicacion', '*' * 4)
	a = leer_int('Ingrese el primer numero')
	b = leer_int('Ingrese el segundo numero')
	print(f'La El resultado de la Multiplicacion es: {a * b}')
	print('**Presione culaquier tecla para salir del Menu***')
def dividir():
	while True:
		try:
			print('*' * 4, 'Dividir', '*' * 4)
			a = leer_int('Ingrese el primer numero')
			b = leer_int('Ingrese el segundo numero')
			print(f'La El resultado de la Division es: {a / b}')
			print('**Presione culaquier tecla para salir del Menu***')
		except ZeroDivisionError:
			print('!Error! No es posible Dividir entre cero ')
def potencia():
	print('*' * 4, 'Potencia', '*' * 4)
	a = leer_int('Ingrese el primer numero')
	b = leer_int('Ingrese el segundo numero')
	print(f'La El resultado de la Potencia es: {a ** b}')
	print('**Presione culaquier tecla para salir del Menu***')
def factorial():
	num = leer_int('')
	f = 1
	for i in range(1,num + 1):
		f *=i
	print(f'''
	El resultado del factorial es:{f}
	
	***Presione culaquier tecla para salir del Menu***
	''')

def salir():
		print('\nGracias por usar mi mini calculadora')
		exit()
# El pograma GENERAL
while True:
	opcion = menu()

	if opcion == 1:
		sumar()
	elif opcion ==2:
		restar()
	elif opcion ==3:
		multiplicar()
	elif opcion ==4:
		dividir()
	elif opcion ==5:
		potencia()
	elif opcion ==6:
		factorial()
	elif opcion ==7:
		salir()
		break
else:
	ms_error('opcion Invalida')


