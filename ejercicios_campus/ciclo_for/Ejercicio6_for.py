'''
La empresa ACME desea calcular el valor de la nómina de N empleados (estos N empleados son
ingresados por el usuario), tanto el sueldo bruto como el sueldo neto. El sueldo bruto se calcula a partir
del valor de la hora y la cantidad de horas trabajadas. A esto se le descuenta el valor de la EPS que es el
4%, el valor de la Pensión que es el 4%. El sueldo neto es el sueldo bruto menos los descuentos. Por
cada empleado se quiere mostrar, el valor del sueldo bruto, cada uno de los descuentos y el valor del
sueldo Neto. Para este ejercicio el valor de la hora es $20.000.

Al final se debe mostrar una estadística con los totales de los salarios brutos, EPS, Pensión y salarios
netos. Luego mostrar el empleado que más gana en salario neto (nombre y salario neto), el empleado
que menos gana en salario neto (nombre y salario neto) y los promedios de sueldos brutos y sueldos
netos.
'''

n = int(input('Digite el numero de empleados a calcular nomina: '))
valor_hora = 20000
sueldo_bruto = 0
descuento_eps = 0
descuento_pension = 0
sueldo_neto = 0
total_s_bruto = 0
total_s_neto = 0
total_eps = 0
total_pension = 0
sueldo_mayor = 0
emple_mayor = ''
sueldo_menor = 9999999999
emple_menor = ''
for i in range(n):
    nombre_empleado = input("Ingrese el nombre del empleado: ")
    horas_trabajadas = int(input(f"Ingrese la cantidad de horas laboradas del empleado {nombre_empleado}: "))
    sueldo_bruto = horas_trabajadas * valor_hora
    total_s_bruto += sueldo_bruto
    descuento_eps = int(sueldo_bruto * 0.04)
    total_eps += descuento_eps
    descuento_pension = int(sueldo_bruto * 0.04)
    total_pension += descuento_pension
    sueldo_neto = sueldo_bruto - descuento_eps - descuento_pension
    total_s_neto += sueldo_neto

    if sueldo_neto > sueldo_mayor:
        sueldo_mayor = sueldo_neto
        emple_mayor = nombre_empleado
    if sueldo_neto < sueldo_menor:
        sueldo_menor = sueldo_neto
        emple_menor = nombre_empleado
        

print('\n', '-' * 25, 'Estadisticas', '-' * 25)
print(
    f"""
    El total del sueldo bruto de todos los empleados es: {format(total_s_bruto, ',')} \n
    El total del sueldo neto de todos los empleados es:  {format(total_s_neto, ',')} \n
    El total de pension a pagar de los empleados es:     {format(total_pension, ',')}\n
    El total de Eps a pagar de los empleados es:         {format(total_pension, ',')}\n  
    """)
print('-' * 65, "\n")

print(f'''
    El empleado {emple_mayor.upper()} tiene el mayor sueldo neto : {sueldo_mayor}\n
    El empleado {emple_menor.upper()} tiene el menor sueldo neto : {sueldo_menor}\n
    El promedio de sueldos brutos de los empleados es: {format(int(total_s_bruto / n), ',')}\n
    El promedio de sueldos netos de los empleados es:  {format(int(total_s_neto / n), ',')}\n
''')
print('-' * 65, "\n")