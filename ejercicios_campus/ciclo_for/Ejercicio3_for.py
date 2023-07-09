'''
Construya un programa tal que encuentre y muestre todos los enteros positivos, comenzando desde el
cero, que satisfacen la siguiente expresión:
p^3+Q^4-2*p^2 < 680
'''

p = int(input('Ingrese el valor de p: '))
q = int(input('Ingrese el valor de q: '))

eva_exp = p ** 3 + q ** 4 - 2 * p ** 2
result = 0
if eva_exp < 680:
    for i in range(eva_exp):
        print(i, end=',')
