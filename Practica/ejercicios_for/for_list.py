# implementacion de un ciclo for dentro una lista para determinar los numeros pares de n numeros 
numeros = []
for i in range(10):
    num = int(input(f'Digite el numero {i}--> '))
    numeros.append(num)

pares = [num for num in numeros if num % 2 == 0]
print(pares)
