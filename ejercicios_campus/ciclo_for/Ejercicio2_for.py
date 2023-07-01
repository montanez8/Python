'''
Construya un programa tal que lea un número entero N, muestre la cantidad de términos y el resultado
de la siguiente serie:
1-1/2+1/3-1/4...=/- 1/N
'''
numero = int(input('Digite un numero: '))

cant_termino = 0
resultado = 0

for i in range(1, numero + 1):
    cant_termino += 1 
    resultado += 1 / i

print('-.-' * 24)
print(f'La cantidad de terminos es: {cant_termino} y el resultado de la series es: {resultado:.4f}')
