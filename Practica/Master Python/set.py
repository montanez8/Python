# set vacio
my_set = set()
# conjunto de elementos
my_set = {1,2,3,4,5,6,7,8}

# agregar elementos a un set
my_set.add(9)

# eliminar elementos de un set 
my_set.remove(5)

# verificar si un elementos existe en el conjunto
if 3 in my_set:
    print("3 está en el conjunto")

# operaciones de conjuntos 
# Union

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.union(set2)  # {1, 2, 3, 4, 5}

# Intersiccion de conjuntos
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.intersection(set2)  # {3}


# diferencia de conjuntos
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.difference(set2)  # {1, 2}

# diferencia simetrica
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.symmetric_difference(set2)  # {1, 2, 4, 5}



