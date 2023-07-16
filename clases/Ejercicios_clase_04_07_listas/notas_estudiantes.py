nota_menor = None
nota_mayor = None 
sum_notas = None
pro_notas = None
list_notas = list()

def leer_float(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("!Error! ingrese un numero")
for est in range(1, 11):
    nota = leer_float(f"Ingrese la nota estudiante #{est}: ")
    list_notas.append(nota)
nota_menor = min(list_notas)
print(f"La nota menor es: {nota_menor}")
nota_mayor = max(list_notas)
print(f"La nota mayor es: {nota_mayor}")

pro_notas = sum(list_notas) / 10
print(f"El promedio de las notas es: {pro_notas}")
list_notas.sort(reverse=True)
tres_notas = list_notas[0:3]
print("Las tres primeras notas es:" ,tres_notas)


