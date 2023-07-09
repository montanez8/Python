'''
Escribe un programa en Python que determine si un año ingresado por el usuario es bisiesto o no. Un
año bisiesto es aquel que es divisible entre 4, excepto aquellos divisibles entre 100 pero no entre 400.
El programa debe realizar lo siguiente:
Solicitar al usuario que ingrese un año.
Verificar si el año cumple con las condiciones para ser bisiesto.
Mostrar un mensaje indicando si el año es bisiesto o no.
'''
year = int(input('Ingrese el año: '))

if year % 4 == 0:
    if year % 400 == 0:
        if year % 100 != 0:
            print('si es un año bisiesto')
        else:
            print('no es un año bisiesto')
    else:
        print('si es un año bisiesto')
else:
    print('No es un año bisiesto')
