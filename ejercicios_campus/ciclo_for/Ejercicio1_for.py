'''
Construya un programa que muestro los números divisibles de 3 y 7 entre 1 y 1000.
'''

divi_tres = []
for i in range(1, 1000):
    if i % 3 == 0 and i % 7:
        divi_tres.append(i)

print(f'Los numeros divisibles entre 3 y 7 son : {divi_tres}')
