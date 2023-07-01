# Adivina el número: Crea un programa en el que la computadora "piense" un número secreto entre 1 y
# 100, y el usuario tenga que adivinarlo. El programa debe proporcionar pistas como "Demasiado bajo"
# o "Demasiado alto" hasta que el usuario adivine correctamente.
# El usuario que gana es el que adivine en el menor número de intentos.

import random as r

n = 1
num_intentos = 0
jugador = int(input('Ingrese la cantidad de jugadores que van a Jugar: '))
while n <= jugador:
	for k in range(1):
		num_intentos = r.randrange(3, 5)
	for i in range(1):
		num_secreto = r.randrange(1, 101)
	numero = 0
	nombre = input('Digite su nombre: ')
	intentos = 1
	ganador = 999999
	nombre_ganador = ''
	while numero != num_secreto and intentos != num_intentos:
			try:
				numero = int(input('Digite un numero:'))
				if numero > 0:
					if numero == num_secreto:
						print('Felicidades adivinaste el numero  ')
						n += 1
					elif numero != num_secreto:
						if numero > num_secreto:
							print('El numero ingresado es demasiado alto')
							intentos += 1
						elif numero < num_secreto:
							print('El numero ingresado es demasiado bajo')
							intentos += 1
					if intentos == num_intentos:
						print('No lo has logrado 😥')
					if intentos < ganador:
						ganador = intentos
						nombre_ganador = nombre
				else:
					print('El numero debe ser mayor a cero')
			except ValueError:
				print('!Error! .Digite un numero valido')

print('-' * 15, 'Ganador 🎉🎉', '-' * 15)
print(f'El ganador es {nombre_ganador} con {ganador} intentos')
