
1. `append()`: Añade un elemento al final de la lista.
   ```python
   lista = [1, 2, 3]
   lista.append(4)
   print(lista)  # Output: [1, 2, 3, 4]
   ```

2. `clear()`: Elimina todos los elementos de la lista.
   ```python
   lista = [1, 2, 3]
   lista.clear()
   print(lista)  # Output: []
   ```

3. `extend()`: Une una lista a otra.
   ```python
   lista1 = [1, 2, 3]
   lista2 = [4, 5, 6]
   lista1.extend(lista2)
   print(lista1)  # Output: [1, 2, 3, 4, 5, 6]
   ```

4. `count()`: Cuenta el número de veces que aparece un elemento en la lista.
   ```python
   lista = [1, 2, 2, 3, 3, 3]
   count = lista.count(2)
   print(count)  # Output: 2
   ```

5. `index()`: Devuelve el índice en el que aparece un elemento.
   ```python
   lista = [1, 2, 3, 4, 5]
   index = lista.index(3)
   print(index)  # Output: 2
   ```

6. `insert()`: Inserta un elemento en una posición específica.
   ```python
   lista = [1, 2, 3]
   lista.insert(1, 4)
   print(lista)  # Output: [1, 4, 2, 3]
   ```

7. `pop()`: Extrae y elimina el último elemento de la lista, o un elemento en una posición específica.
   ```python
   lista = [1, 2, 3, 4, 5]
   elemento = lista.pop()
   print(elemento)  # Output: 5
   print(lista)  # Output: [1, 2, 3, 4]
   ```

8. `remove()`: Elimina la primera aparición de un elemento en la lista.
   ```python
   lista = [1, 2, 3, 2, 4]
   lista.remove(2)
   print(lista)  # Output: [1, 3, 2, 4]
   ```

9. `reverse()`: Invierte el orden de los elementos en la lista.
   ```python
   lista = [1, 2, 3, 4, 5]
   lista.reverse()
   print(lista)  # Output: [5, 4, 3, 2, 1]
   ```