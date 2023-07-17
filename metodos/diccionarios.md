

- **len()**: Este método se utiliza para contar la longitud de un diccionario, es decir, el número de pares clave-valor que contiene

  ```python
  teclado = {'Categoría': 'Teclados', 'Modelo': 'HyperX Alloy FPS Pro', 'Precio': '89,99'}
  print(len(teclado)) # Output: 3
  ```

- **get()**: Este método se utiliza para obtener el valor asociado a una clave en un diccionario. Si la clave no existe, se puede especificar un valor predeterminado que se devolverá en su lugar.

  ```python
  teclado = {'Categoría': 'Teclados', 'Modelo': 'HyperX Alloy FPS Pro', 'Precio': '89,99'}
  modelo = teclado.get('Modelo', 'No se encontró el modelo')
  marca = teclado.get('Marca', 'No se encontró la marca')
  print(modelo) # Output: HyperX Alloy FPS Pro
  print(marca) # Output: No se encontró la marca
  ```

- **keys()**: Este método se utiliza para obtener una lista de todas las claves en un diccionario

  ```python
  teclado = {'Categoría': 'Teclados', 'Modelo': 'HyperX Alloy FPS Pro', 'Precio': '89,99'}
  claves = teclado.keys()
  print(claves) # Output: dict_keys(['Categoría', 'Modelo', 'Precio'])
  ```

- **values()**: Este método se utiliza para obtener una lista de todos los valores en un diccionario. 

  ```python
  teclado = {'Categoría': 'Teclados', 'Modelo': 'HyperX Alloy FPS Pro', 'Precio': '89,99'}
  valores = teclado.values()
  print(valores) # Output: dict_values(['Teclados', 'HyperX Alloy FPS Pro', '89,99'])
  ```

- **items()**: Este método se utiliza para obtener una lista de todos los pares clave-valor en un diccionario.

  ```python
  teclado = {'Categoría': 'Teclados', 'Modelo': 'HyperX Alloy FPS Pro', 'Precio': '89,99'}
  items = teclado.items()
  print(items) # Output: dict_items([('Categoría', 'Teclados'), ('Modelo', 'HyperX Alloy FPS Pro'), ('Precio', '89,99')])
  ```

- **update()**: Este método se utiliza para actualizar un diccionario con otro diccionario o con pares clave-valor.

  ```python
  teclado = {'Categoría': 'Teclados', 'Modelo': 'HyperX Alloy FPS Pro', 'Precio': '89,99'}
  teclado_nuevo = {'Precio': '99,99', 'Color': 'Negro'}
  teclado.update(teclado_nuevo)
  print(teclado) # Output: {'Categoría': 'Teclados', 'Modelo': 'HyperX Alloy FPS Pro', 'Precio': '99,99', 'Color': 'Negro'}
  ```

- **pop()**: Este método se utiliza para eliminar un par clave-valor de un diccionario y devolver el valor asociado a la clave. Si la clave no existe, se puede especificar un valor predeterminado que se devolverá en su lugar.

  ```python
  teclado = {'Categoría': 'Teclados', 'Modelo': 'HyperX Alloy FPS Pro', 'Precio': '89,99'}
  precio = teclado.pop('Precio', 'No se encontró el precio')
  marca = teclado.pop('Marca', 'No se encontró la marca')
  print(precio) # Output: 89,99
  print(marca) # Output: No se encontró la marca
  ```
