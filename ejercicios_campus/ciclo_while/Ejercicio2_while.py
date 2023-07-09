'''
De una serie de números ingresados por el usuario, imprima cuales de estos son primos y cuáles no.
El ingreso de los números se termina cuando el usuario ingrese un numero negativo.
'''
numero = 1
cont = 0
while numero >= 0:
    
    numero = int(input('Digite un numero --> '))
    for i in range(2, numero):
        modulo = numero % i
        if modulo == 0:
            cont += 1
    print('-' * 24)
    if cont == 0:
        print(f'El numero {numero} es Primo'.upper())
    else:
        print(f'El numero {numero} no es Primo'.upper())
    print('-' * 24)
else:
    print('El numero tiene que ser entero positivo ')
    
    
    
    
    
