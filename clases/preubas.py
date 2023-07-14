# Dict para almacenar los productos
productos = {}

# Función para agregar un nuevo producto


def agregar_producto(codigo, valor_unitario, tipo_iva):
    productos[codigo] = {
        "valor_unitario": valor_unitario,
        "tipo_iva": tipo_iva
    }

# Función para procesar la compra de un cliente


def procesar_compra():

    total = 0
    total_iva = 0

    while True:
        codigo = input("Ingrese código del producto (0 para finalizar): ")
        if codigo == '0':
            break

        if codigo not in productos:
            print("Producto no existe")
            continue

        cantidad = int(input("Ingrese cantidad: "))
        prod = productos[codigo]

        valor = cantidad * prod["valor_unitario"]
        if prod["tipo_iva"] == 1:
            iva = 0
        elif prod["tipo_iva"] == 2:
            iva = valor * 0.05
        else:
            iva = valor * 0.19

        valor_total = valor + iva
        print(f"{codigo} - Valor: {valor} - IVA: {iva} - Total: {valor_total}")

        total += valor
        total_iva += iva

    print(f"Total: {total}")
    print(f"Total IVA: {total_iva}")
    print(f"Total con IVA: {total + total_iva}")


# Menú principal
while True:
    print("Menú:")
    print("1. Agregar producto")
    print("2. Procesar compra")
    print("0. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == '1':
        codigo = input("Ingrese código del producto: ")
        valor_unitario = float(input("Ingrese valor unitario: "))
        tipo_iva = int(input("Ingrese tipo de IVA (1 - 2 - 3): "))
        agregar_producto(codigo, valor_unitario, tipo_iva)
    elif opcion == '2':
        procesar_compra()
    elif opcion == '0':
        break
