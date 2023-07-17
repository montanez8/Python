
- **len()**: Este método devuelve la longitud de una cadena, es decir, el número de caracteres que contiene.

```python
cadena = "Hola mundo"
longitud = len(cadena)
print(longitud) # Output: 10
```

- **lower()**: Este método convierte\*\* \*\*todos los caracteres de una cadena a minúsculas

```python
cadena = "Hola Mundo"
nueva_cadena = cadena.lower()
print(nueva_cadena) # Output: hola mundo
```

- **upper()**: Este método convierte todos los caracteres de una cadena a mayúsculas.

```python
cadena = "Hola Mundo"
nueva_cadena = cadena.upper()
print(nueva_cadena) # Output: HOLA MUNDO
```

- **replace()**: Este método reemplaza todas las ocurrencias de un substring en una cadena con otro substring.

```python
cadena = "Hola Mundo"
nueva_cadena = cadena.replace("Mundo", "Python")
print(nueva_cadena) # Output: Hola Python
```

- **split()**: Este método divide una cadena en una lista de substrings, utilizando un separador especificado.

```python
cadena = "Hola,Mundo"
lista = cadena.split(",")
print(lista) # Output: ['Hola', 'Mundo']
```

- **find()**: Este método busca la primera ocurrencia de un substring en una cadena y devuelve su posición. Si el substring no se encuentra, devuelve -1.

```python
cadena = "Hola Mundo"
posicion = cadena.find("Mundo")
print(posicion) # Output: 5
```

- **isdigit()**: Este método devuelve True si todos los caracteres de una cadena son dígitos numéricos.

```python
cadena = "12345"
es_digito = cadena.isdigit()
print(es_digito) # Output: True
```

- **isalpha()**: Este método devuelve True si todos los caracteres de una cadena son letras.

```python
cadena = "HolaMundo"
es_letra = cadena.isalpha()
print(es_letra) # Output: True
```

- **strip()**: Este método elimina los espacios en blanco al principio y al final de una cadena.

```python
cadena = "   Hola Mundo   "
nueva_cadena = cadena.strip()
print(nueva_cadena) # Output: Hola Mundo
```
