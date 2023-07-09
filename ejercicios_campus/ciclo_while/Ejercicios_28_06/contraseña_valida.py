# Hacer un programa que pida al usuario un texto como contraseña y el programa debe validar si es válida.
# Una contraseña es válida si:
# • Tiene una longitud mínima de 8 caracteres
# • Debe contener una letra en minúscula
# • Debe contener una letra en mayúscula
# • Debe contener un número
# • No puede contener espacios
# • Debe tener por lo menos uno de los siguientes caracteres especiales (%^&)
import re
correcta = False
valid_min = False
valid_may = False
valid_num = False
valid_sp = False
valid_esp = False
while True:
	password = input('''
		Digite una contraseña con las siguientes caracteristicas:
			• Tiene una longitud mínima de 8 caracteres
			• Debe contener una letra en minúscula
			• Debe contener una letra en mayúscula
			• Debe contener un número
			• No puede contener espacios
			• Debe tener por lo menos uno de los siguientes caracteres especiales (%^&)
			-->
	''')
	if len(password) >= 8:
		for i in password:
			if re.search(r'[a-z]',i):
				valid_min = True
			if re.search(r'[A-Z]',i):
				valid_may = True
			if re.search(r'\d',i):
				valid_num = True
			if i == '%' or i == '&':
				valid_sp = True
			if i == ' ':
				valid_esp = True
		if valid_min == True and valid_may == True and valid_sp == True and valid_esp == False:
			print('La contraseña es Correcta')
			break
		elif valid_min == False:
			print('La contraseña debe contener una minuscula')
		elif valid_may == False:
			print('La contraseña debe contener una Mayuscula')
		elif valid_num == False:
			print('La contraseña debe contener un numero')
		elif valid_sp == False:
			print('La contraseña no debe contener un espacio')
	else:
		print('Longitud invalida tiene que ser minimo  8 caracteres')
