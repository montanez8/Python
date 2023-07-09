""" Diseñe y escriba un programa que solicite tres números enteros (pueden ser positivos o negativos) y
como salida los muestre en orden de mayor a menor """

num_1 = int(input('Digite el primer numero: '))
num_2 = int(input('Digite el segundo numero: '))
num_3 = int(input('Digite el tercer numero: '))
print('\n', '-*-'*30)
if num_1 > num_2 and num_1 > num_3:
    if num_2 > num_3:
        print(f'    Mayor a menor {num_1} {num_2} {num_3}')
    elif num_1 > num_3 and num_3 > num_2:
        print(f'    Mayor a menor {num_1} {num_3} {num_2}')
    elif num_2 == num_3:
        print(f'    Mayor a menor {num_1} {num_3} {num_2}')
elif num_2 > num_1 and num_2 > num_3:
    if num_1 > num_3:
        print(f'    Mayor a menor {num_2} {num_1} {num_3}')
    if num_2 > num_3 and num_2 > num_1:
        print(f'    Mayor a menor {num_2} {num_3} {num_1}')
else:
    print(f'    Mayor a menor {num_3} {num_2} {num_1}')
