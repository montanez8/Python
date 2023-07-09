# encontrar los tres caracteres mas comunes 
# tres mas comunes junto al numero de ocurrencias
# ordenar de forma descendente
# si recuentro de ocurreencias es el mismo ordenar de forma alfabetica

palabra = input("Ingrese una palabra: ")
caracter = {}
for char in palabra:
    caracter[char] = caracter.get(char,0) + 1

repet_values = sorted([(v,k) for k,v in caracter.items()], reverse=True)

for char , cant in repet_values[:3]:
    print(cant , char)