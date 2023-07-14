import json

productos = []

while True:
    codigo = input("Ingrese el código del producto: ")
    if codigo == "":
        break

    valor_unitario = float(input("Ingrese el valor unitario del producto: "))
    cantidad_comprada = int(input("Ingrese la cantidad comprada: "))
    tipo_iva = int(input("Ingrese el tipo de IVA (1=Exento, 2=Bienes, 3=General): "))

    productos.append({
        "codigo": codigo,
        "valor_unitario": valor_unitario,
        "cantidad_comprada": cantidad_comprada,
        "tipo_iva": tipo_iva
    })

with open("productos.json", "w") as archivo:
    json.dump(productos, archivo)
