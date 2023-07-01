# Autor: Carlos Montañez
'''
Construya un programa que lea 10 números ingresados por el usuario y que al final, muestre el mayor
y el menor de todos estos números.
'''

mayor = 0
menor = 9999999
for i in range(1, 11):
    numeros = int(input(f'Digite un numero:{i}: '))
    if numeros > mayor:
        mayor = numeros

    if numeros < menor:
        menor = numeros
print('-' * 30, '\n El mayor numero  es:', mayor, '\n El menor numero es: ', menor, '\n', '-' * 30)
