def leer_int(msg):
	while True:
		try:
			n = int(input(msg))
			return n
		except ValueError:
			print('!Error! Ingrese un numero valido')
def media(n1 , n2 , n3):
	m = n1 + n2 + n3 / 3
	return m

a = leer_int('ingrese el primer numero')
b = leer_int('ingrese el segundo numero')
c = leer_int('ingrese el tercer numero')


print(f'La media de los tres numeros es: {media(a , b ,c):.3f}')