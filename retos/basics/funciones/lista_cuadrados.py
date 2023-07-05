'''
Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.
'''
def calcular_cuadrados(lista_num = []):
    cuadrados = []
    for i in lista_num:
        cuadrados.append(i ** 2)
        
    return cuadrados


lista_num = []
while True:
    numero = int(input("Dgite un numero para agregarlo a la lista y calcular su cuadrado: "))
    if numero !=0:
        lista_num.append(numero)
        continue
    else:
        break
    
    
print(f"La lista numeros es {lista_num} y sus cuadras es {calcular_cuadrados(lista_num)}")