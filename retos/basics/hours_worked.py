# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
# Después debe mostrar por pantalla la paga que le corresponde.

number_hours = int(input('enter number of hours worked: '))
cost_hours = int(input('enter the cost of each hour: '))

pay = cost_hours * number_hours
print(f'he pay you are entitled to is {pay}')