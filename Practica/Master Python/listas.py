# crear una lista
colores = ["rojo","amarillo","azul","verde"]

# acceder a un elemento de la lista
# donde [1] es el elemento al que vamos acceder salida = amarillo
#  tambien se puede acceder desde el ultimo elemento con -1 ,...
colores[1]

# mostar un elemento de la lista y acceder a un caracter especifico}

char =colores[1][0]
print(char)

# cambiar un elemento de la lista
colores[1]="gris"
print(colores)

# añadir un elemento a la lista
colores.append("Amarillo")
print(colores)

# insertar un valor en una posicion especifica

colores.insert(0,"naranja")
print(colores)

# vaciar lista
# colores.clear()
# print(colores)

# eliminar un elemento de la lista colores.pop("posicion") .remove(elemento)

numeros = [1,2,3,4,5,6,7,8,2]
# copiar o clonar una lista en otra lista
numeros2 = numeros.copy() 
print(numeros2)

# # de veces que se repite un elemento en la lista
print("tiene ",numeros2.count(2))


# buscar elemento con el index
print(numeros2.index(2))

# invertir lista 
colores.reverse()
print(colores)

# ordenar alfabeticamnete 
colores.sort()
print(colores)

# unir dos listas
colores.extend(numeros2)
print(colores)
