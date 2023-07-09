'''
Escribir un programa en el que a partir de una fecha introducida por teclado con el formato DIA-
MES-AÑO, se obtenga la fecha del día siguiente.
Para realizar el cálculo de forma correcta se debe tener en cuenta que hay meses con 30 días y otros
con 31 y que febrero puede tener 29 si es bisiesto el año.
'''
dia = int(input('Ingrese el dia: '))
mes = int(input('Ingrese el mes: (formato numero): '))
year = int(input('Ingrese el año: '))

if year % 4 == 0:
    if year % 400 == 0:
        if year % 100 != 0:
            bisiesto = True
        else:
            bisiesto = False
    else:
        bisiesto = True
else:
    bisiesto = False

print(bisiesto)

if mes == 2:
    if bisiesto:
        dias_mes = 29
    else:
        dias_mes = 28
elif mes in [4, 6, 9, 11]:
    dias_mes = 30
else:
    dias_mes = 31

if dia == dias_mes:
    dia = 1
    if mes == 12:
        mes = 1
        year += 1
    else:
        mes += mes
else:
    dia += 1

print(f'La fecha del día siguiente es: {dia}-{mes}-{year}')
