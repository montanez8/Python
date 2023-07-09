nombre_conductor = input("Ingrese el nombre del conductor ")
placa_vehiculo = input("Ingrese la placa del vehiculo ")
valor_pasaje = int(input("Ingrese el valor del pasaje "))
valor_encomiendas = int(input("Ingrese el valor de las encomiendas "))
valor_concepto_pasaje = int(valor_pasaje * 0.25)
valor_concepto_encomienda = int(valor_encomiendas * 0.15)

print("Nombre conductor: ", nombre_conductor)
print("Placa del vehiculo: ", placa_vehiculo)
print(
    f"Valor pasaje: {valor_pasaje}  Valor total por concepto de pasajes: {valor_concepto_pasaje}")

print(
    f"Valor encomiendas: {valor_encomiendas} valor por concepto de encomiendas: {valor_concepto_encomienda}")

print(
    f"Valor total a pagar conductor: {valor_pasaje + valor_encomiendas + valor_concepto_pasaje + valor_concepto_encomienda}")


