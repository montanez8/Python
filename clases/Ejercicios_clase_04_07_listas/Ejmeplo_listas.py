mi_lista = []
print(mi_lista)
mi_lista.append("alirio")
print(mi_lista)

mi_lista.extend(["Andres","Carlos","Cristian","Diana"])
print(mi_lista , len(mi_lista))

mi_lista.pop()

mi_lista.insert(2,"liliam")

print(mi_lista)

mi_lista.remove("Carlos")

# operaciones de listas

# recorrido por index

print("\n")
for i in range(len(mi_lista)):
    print(i ,"-->" , mi_lista[i])
    
print("\n")

for i in mi_lista:
    print(i , end=" ")
    
# buscar un elemento 

print("\n","-" * 45 )

def buscar_elemento(lis , elem):
    for i in range(len(lis)):
        if lis[i] == elem:
            return i
    return -1


print(buscar_elemento(mi_lista,"Cristian"))


#  buscar un elemento en la lista == True != False

def encontrar_element(lis , elemen):
    for i in lis:
        if i == elemen:
            return True
    return False

print(encontrar_element(mi_lista , "alirio"))



    
    
