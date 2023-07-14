# facturacion al cliente
# ingreso de productos con sus datos
# • Código del producto.
# • Valor unitario del producto
# • Cantidad comprada.
# • Tipo de IVA, que puede ser:
# ◦  1: Exento de IVA
# ◦  2: Bienes, donde se aplica como IVA el 5%
# ◦  3: General, donde se aplica como IVA el 19%
#  Si ingresa un código de producto que no exista, no debe permitir la venta al cliente y mostrar un mensaje que indique que
#  ese producto no existe.


import json


def guardar_producto(productos):
    while True:
        cod_product = int(input('Digite codigo Producto: '))
        nombre_product = input('Nombre Producto: ')
        valor_unit_pro = float(input('Valor unitario producto: '))
        cant = int(input('Cantidad existente del producto: '))

        while True:
            iva = int(input(
                'Seleccione el tipo de iva del Producto:\n1.Exento de Iva \n2.Bienes \n3.General : '))
            if iva in [1, 2, 3]:
                iva = tipo_iva(iva)
                break
            else:
                print('Opcion no valida')
                continue
        productos[cod_product] = {'nombre_producto': nombre_product,
                                  'valor_initario': valor_unit_pro, 'cantidad': cant, 'iva': iva}
        op = input('Desea agregar otro Producto SI/NO: ').upper()
        if op == 'SI':
            continue
        break
    with open('productos.json', 'w') as prod:
        json.dump(productos, prod, indent=4)
    return productos


def cargar_productos():
    try:
        productos = {}
        with open('productos.json', 'r') as pro:
            productos = json.load(pro)
            return productos
    except FileNotFoundError:
        productos = {}
        return productos


def tipo_iva(tipo_iva):
    iva = 0
    if tipo_iva == 1:
        iva = 0
    elif tipo_iva == 2:
        iva = 0.05
    elif tipo_iva == 3:
        iva = 0.19
    return iva


def lista_productos(productos):
    print("-"*15, "Listado de Productos", "-"*15)
    for i, (cod, producto) in enumerate(productos.items()):
        if i % 5 == 0 and i != 0:
            opcion = input("¿Desea seguir viendo? (s/n): ")
            if opcion.lower() != "s":
                return
        print("ID            : ", cod)
        print("Nombre        : ", producto['nombre_producto'])
        print("Valor unitario: ", producto['valor_initario'])
        print("Cantidad      : ", producto['cantidad'])
        print("-"*50, "\n")


def validar_cod_product(cod, productos):
    return cod not in productos


def cargar_ventas():
    try:
        ventas = {}
        with open('ventas.json', 'r') as pro:
            ventas = json.load(pro)
            return ventas
    except FileNotFoundError:
        ventas = {}
        return ventas


def compra_cliente(productos, ventas):
    comprados = {}
    productos = cargar_productos()
    while True:
        cod = int(input("Ingrese el codigo del producto a vender: "))
        if cod in productos:
            producto = productos[cod]
            cod_product = cod
            nombre_product = producto['nombre_producto']
            valor_unit_pro = producto['valor_initario']
            cant = producto['cantidad']
            iva = producto['iva']
            ventas[cod_product] = {'nombre_producto': nombre_product,'valor_initario': valor_unit_pro, 'cantidad': cant, 'iva': iva}
            op = input('Va a vender otro Producto SI/NO: ').upper()
            if op == 'SI':
                continue
            break
        else:
            print("Producto sin Existencias")
        with open('ventas.json', 'w') as prod:
            json.dump(productos, prod, indent=4)


def imprimir_factura():
    pass


def datos_clientes():
    pass


def informe():
    pass


def continuar():
    input('Ingrese cualquier tecla para continuar')


def menu():
    productos = cargar_productos()
    ventas = cargar_ventas()
    while True:
        try:
            print('*** NOMINA ACME ***')
            print('MENU')
            print('1- Agregar Productos')
            print('2- Vender Productos')
            print('3- Informe Ventas')
            print('4- Salir')
            opcion = int(input('Escoja una opción (1-8)? '))
            if opcion == 1:
                guardar_producto(productos)
                lista_productos(productos)
                continuar()
            elif opcion == 2:
                compra_cliente(productos ,ventas)
                continuar()
            elif opcion == 3:
                continuar()
            elif opcion == 4:
                continuar()
                print('Hasta Luego..')
                break
        except ValueError:
            print('\nIngrese una opcion Valida\n')
            continuar()


if __name__ == '__main__':
    menu()
