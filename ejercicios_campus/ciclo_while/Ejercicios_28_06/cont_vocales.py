# Contador de vocales: Crea un programa que solicite al usuario ingresar una frase y cuente la cantidad
# total de vocales en ella. Utiliza un ciclo "while" para recorrer cada letra de la frase. Si una vocal es
# encontrada, incrementa el contador de vocales. Sin embargo, si el usuario ingresa la letra 'q', el programa
# debe terminar y mostrar la cantidad total de vocales encontradas hasta ese momento.

frase = input('Ingrse una frase ')
cont_vocal = 0
#for i in frase:
i = 0
while i < len(frase):
	letra = frase[i].lower()
	if letra == 'q':
		break
	if letra in 'aeiou':
		cont_vocal += 1
	i += 1
print(f'La cantidad de vocales en la frase es: {cont_vocal}')
