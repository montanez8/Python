import json
import os

# Definir las estructuras de datos
productos = {}
clientes = {}
ventas = []

# Cargar la información
if os.path.exists('productos.json'):
    with open('productos.json', 'r') as f:
        productos = json.load(f)
if os.path.exists('clientes.json'):
    with open('clientes.json', 'r') as f:
        clientes = json.load(f)
if os.path.exists('ventas.json'):
    with open('ventas.json', 'r') as f:
        ventas = json.load(f)


def guardar_informacion():
    with open('productos.json', 'w') as f:
        json.dump(productos, f)
    with open('clientes.json', 'w') as f:
        json.dump(clientes, f)
    with open('ventas.json', 'w') as f:
        json.dump(ventas, f)


def mostrar_menu():
    print('1. Ingresar producto')
    print('2. Ingresar cliente')
    print('3. Realizar venta')
    print('4. Mostrar información')
    print('5. Salir')

def ingresar_producto():
    codigo = input('Ingrese el código del producto: ')
    if codigo in productos:
        print('El código del producto ya existe')
        return
    valor_unitario = float(input('Ingrese el valor unitario del producto: '))
    cantidad = int(input('Ingrese la cantidad disponible del producto: '))
    tipo_iva = int(input('Ingrese el tipo de IVA (1: Exento, 2: Bienes): '))
    productos[codigo] = {
        'valor_unitario': valor_unitario,
        'cantidad': cantidad,
        'tipo_iva': tipo_iva
    }
    guardar_informacion()
    print('Producto ingresado correctamente')

def ingresar_cliente():
    identificacion = input('Ingrese el número de identificación del cliente: ')
    if identificacion in clientes:
        print('El cliente ya existe')
        return
    nombre = input('Ingrese el nombre del cliente: ')
    clientes[identificacion] = {
        'nombre': nombre
    }
    guardar_informacion()
    print('Cliente ingresado correctamente')

# Función para realizar una venta


def realizar_venta():
    identificacion = input('Ingrese el número de identificación del cliente: ')
    if identificacion not in clientes:
        print('El cliente no existe')
        return
    total_factura = 0
    total_iva = 0
    while True:
        codigo = input(
            'Ingrese el código del producto (o "0" para terminar): ')
        if codigo == '0':
            break
        if codigo not in productos:
            print('El código del producto no existe')
            continue
        cantidad = int(input('Ingrese la cantidad del producto: '))
        if cantidad > productos[codigo]['cantidad']:
            print('No hay suficiente cantidad disponible')
            continue
        valor_unitario = productos[codigo]['valor_unitario']
        tipo_iva = productos[codigo]['tipo_iva']
        valor_producto = valor_unitario * cantidad
        if tipo_iva == 1:
            valor_iva = 0
        elif tipo_iva == 2:
            valor_iva = valor_producto * 0.05
        valor_final = valor_producto + valor_iva
        total_factura += valor_final
        total_iva += valor_iva
        productos[codigo]['cantidad'] -= cantidad
        ventas.append({
            'identificacion': identificacion,
            'codigo': codigo,
            'cantidad': cantidad,
            'valor_unitario': valor_unitario,
            'valor_iva': valor_iva,
            'valor_final': valor_final
        })
    guardar_informacion()
    print('Venta realizada correctamente')
    print('Total factura: $', total_factura)
    print('Total IVA: $', total_iva)

# Función para mostrar la información


def mostrar_informacion():
    opcion = input('Ingrese la opción (\n1: Cantidad de productos vendidos\n'
                    '2: Valor total de los productos vendidos sin IVA\n'
                    '3: Valor total del IVA de los productos vendidos\n'
                    '4: Valor total de los productos vendidos con IVA)\n: ')
    if opcion == '1':
        cantidad_vendida = sum([venta['cantidad'] for venta in ventas])
        print('Cantidad de productos vendidos:', cantidad_vendida)
    elif opcion == '2':
        valor_sin_iva = sum(
            [venta['valor_unitario'] * venta['cantidad'] for venta in ventas])
        print('Valor total de los productos vendidos sin IVA: $', valor_sin_iva)
    elif opcion == '3':
        valor_iva = sum([venta['valor_iva'] for venta in ventas])
        print('Valor total del IVA de los productos vendidos: $', valor_iva)
    elif opcion == '4':
        valor_con_iva = sum([venta['valor_final'] for venta in ventas])
        print('Valor total de los productos vendidos con IVA: $', valor_con_iva)
    else:
        print('Opción inválida')


# Ciclo principal del programa
while True:
    mostrar_menu()
    opcion = input('Ingrese la opción: ')
    if opcion == '1':
        ingresar_producto()
    elif opcion == '2':
        ingresar_cliente()
    elif opcion == '3':
        realizar_venta()
    elif opcion == '4':
        mostrar_informacion()
    elif opcion == '5':
        break
    else:
        print('Opción inválida')

# Guardar la información del día actual
guardar_informacion()
