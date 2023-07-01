nombre_empleado = input("Ingrese el nombre del empleado: ")
horas_trabajadas = int(
    input("Ingrese la cantidad de horas laboradas del empleado: "))
valor_hora = 20000
sueldo_bruto = horas_trabajadas * valor_hora
descuento_eps = int(sueldo_bruto * 0.04)
descuento_pension = int(sueldo_bruto * 0.04)
sueldo_neto = sueldo_bruto - descuento_eps - descuento_pension

print(
    f"""
    Valor sueldo bruto: {sueldo_bruto} \n 
    valor del descuento eps: {descuento_eps} \n 
    Valor descuento pension: {descuento_pension} \n 
    Valor sueldo neto {sueldo_neto}
    """)
