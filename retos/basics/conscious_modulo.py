'''
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> 
da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, 
y <c> y <r> son el cociente y el resto de la división entera respectivamente.
'''
print('type two whole numbers')
number_one = int(input('number one: '))
number_two = int(input('number two: '))

conscius = number_one // number_two
modulo = number_one % number_two


print(f'{number_one} entre {number_two} da un conciente de {conscius} y un resto de {modulo}')

