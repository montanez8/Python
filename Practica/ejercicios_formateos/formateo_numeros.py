numero = 100000

# Dos decimales de precisión:
print(format(numero, '0.2f'))

# Jusitificación a la derecha con diez caracteres, un decimal de precisión:
print(format(numero, '>10.1f'))

# Jusitificación a la izquierda con diez caracteres, un decimal de precisión:
print(format(numero, '<10.1f'))

# Separador de miles:
print(format(numero, ','))
print(format(numero, '0,.1f'))

# Notación científica:
print(format(numero, 'e'))
print(format(numero, '0.2E'))