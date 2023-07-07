articulos = {1:"Lapiz",2:"Cuadernos",3:"Borrador",4:"Calculadora",5:"Escuadra"}
valores = {1:2500,2:3800,3:1200,4:35000,5:3700}

def menu_art(art , val):
    print("Lista de productos")
    for codigo , articulo  in art.items():
        print(f"{codigo}. {articulo} - ${valores[codigo]:,}")

compra = {} 
total_compra = 0 

while True:
    menu_art(articulos , valores)
    codigo = int(input("Ingrese el código del artículo a comprar (0 para terminar): "))
    if codigo == 0:
        break
    if codigo not in articulos:
        print("Código de artículo no válido. Intente de nuevo.")
        continue
    cantidad = int(input("Ingrese la cantidad de artículos: "))
    compra[articulos[codigo]] = cantidad * valores[codigo]
    total_compra += compra[articulos[codigo]]

print("\nDetalle de la compra:")
for articulo, valor in compra.items():
    print(f"Artículo: {articulo}, Valor: {valor}")

print(f"\nValor total de la compra: {total_compra}")
