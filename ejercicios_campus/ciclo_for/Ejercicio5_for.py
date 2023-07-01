'''
Construya un programa que me ayude a encontrar el próximo número de la siguiente serie.
1,1,2,-1,1,-2,?
'''

num_uno = 1
num_dos = 1
sgt_num = [1, 1]
for i in range(1, 4):
    operacion = num_uno + num_dos
    num_uno = operacion
    sgt_num.append(operacion)
    for j in range(1):
        diferencia = num_dos - operacion
        sgt_num.append(diferencia)
        num_dos = diferencia

print(sgt_num)
