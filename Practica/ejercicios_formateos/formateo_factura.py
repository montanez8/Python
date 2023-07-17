# Datos de entrada
nombre_cliente = "Juan Pérez"
fecha = "17/07/2023"
productos = [
    {"nombre": "Producto 1", "cantidad": 2, "precio": 10.5},
    {"nombre": "Producto 2", "cantidad": 1, "precio": 5.0},
    {"nombre": "Producto 3", "cantidad": 3, "precio": 2.75},
]

# Cálculo del total
total = sum([p["cantidad"] * p["precio"] for p in productos])

# Impresión de la factura
print("Factura")
print("Cliente:", nombre_cliente)
print("Fecha:", fecha)
print("")

print("{:<20} {:<10} {:<10} {:<20}".format("Producto", "Cantidad", "Precio", "Subtotal"))
print("-" * 50)
for p in productos:
    subtotal = p["cantidad"] * p["precio"]
    print("{:<20} {:<10} {:<10} {:<10}".format(p["nombre"], p["cantidad"], p["precio"], subtotal))
print("-" * 50)
print("{:>40} {:<10}".format("Total:", total))

