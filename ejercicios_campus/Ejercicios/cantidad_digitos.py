'''
Escriba un programa que reciba un número entero positivo y muestre en pantalla la cantidad de dígitos
que este tiene.
No puede convertir el número a cadena, ni usar funciones de cadena. Solo operadores aritméticos.
'''
numero = int(input('Ingrese un numero: '))

can_digitos = 0

# while (numero >= 1):
#     numero = numero / 10
#     can_digitos = can_digitos+1

# print(f'La cantidad de digitos es: {can_digitos}')

if numero == 0:
    can_digitos = 1
else:
    while numero > 0:
        if numero < 10:
            can_digitos = can_digitos + 1
            break
        else:
            numero = numero / 10
            can_digitos = can_digitos + 1

print(f"La cantidad de dígitos es: {can_digitos}")


