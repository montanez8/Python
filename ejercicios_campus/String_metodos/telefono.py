# los telefonos de la una empresa tienen el siguiente formato
# prefijo-numero-expension donde el prefijo es el codigo del pais +34
# y la extension tiene dos digitos --> +34-913724710-56
# Escribe un pograma que pregunte por un numero de telefono con el formato
# y muestre por pantalla el numero de telefono sin el prefijo y la extension.

while True:
	telefono = input("Introduce el número de teléfono con el formato +34-913724710-56: ")
	if telefono.strip() == '':
		continue
	break

telefono = telefono.split('-')
telefono = telefono[1]
print(f'Su numero de telefono sin extension y prefijo es: {telefono}')
