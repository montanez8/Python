'''
Se ingresan los nombres y notas de estudiantes, indique cual es el promedio del curso, cual es el
estudiante con mayor y menor nota (nombre y nota).
El ingreso se termina cuando el profesor ingrese FIN en el nombre.
'''

nombre = ''
nota = 0
nota_mayor = 0
nota_menor = 9999999    
sum_notas = 0
cont_st = 0
nom_mayor = ''
nom_menor = ''
while nombre != 'FIN':
    nombre = input('Ingrese el nombre del estudiante: ').upper()
    if nombre != 'FIN':
        nota = float(input('Ingrese la nota del estuduante: '))
        sum_notas += nota
        cont_st += 1

        if nota > nota_mayor:
            nota_mayor = nota
            nom_mayor = nombre
        if nota < nota_menor:
            nota_menor = nota
            nom_menor = nombre

print('''
El promedio de las notas del curso es: {}
El estudiante {} tiene la mayor nota: {}
El estudiante {} tiene la menor nota: {} 

'''.format((sum_notas / cont_st).__round__(2), nom_mayor, nota_mayor, nom_menor, nota_menor))
