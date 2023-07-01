# determine el mayor numero de N valores ingresados
valores = int(input('Escriba la cantidad de valores: '))
valor_max = 0
valor_min = 9999
for i in range(1,valores+1):
    num = int(input(f'Ingrese el numero {i} --> '))
    if num > valor_max:
        valor_max = num
    if num < valor_min:
        valor_min = num
        
        
print(f'El mayor numero es: {valor_max}',
      f'El menor nuimero es: {valor_min}')
    