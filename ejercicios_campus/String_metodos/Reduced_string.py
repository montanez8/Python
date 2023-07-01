while True:
	s = input('Digite una cadena de caracteres: ')
	if s.strip() == '':
		continue
	break
i = 0
caracter = ''
string = ''
cont_caracter = 0

for i in s:
	caracter = i
	if caracter == i:
		cont_caracter += 1
		string = s.replace(caracter, ' ')
		print(string)
