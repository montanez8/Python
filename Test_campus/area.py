
import math as m
'''
Algoritmo que nos calcule el área de un triángulo conociendo sus lados. La estructura selectiva
se utiliza para el control de la entrada de datos en el programa. Para calcular el área, usar la

p > a ∧ p > b ∧ p > c ; (∧ es el símbolo de y − and−)
'''

a = float(input('Digite el lado 1 del triangulo: '))
b = float(input('Digite el lado 2 del triangulo: '))
c = float(input('Digite el lado 3 del triangulo: '))

p = (a + b + c)/2
if p > a and p > b and p > c :
    area = m.sqrt(p*(p-a)*(p-b)*(p-c))
    print(f'El area del triangulo es: {area}')
else:
    print('Medidas incorrectas')
    
