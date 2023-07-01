'''
Mostrar en pantalla si dos números enteros positivos n1 y n2 son amigos. Los números amigos son pares
de números enteros positivos en los cuales la suma de los divisores propios de cada número es igual al
otro número. En otras palabras, dos números amigos cumplen la condición de que la suma de los
divisores propios de uno de ellos es igual al otro número, y viceversa. Por ejemplo, el par de números
(220, 284) es un par de números amigos. Los divisores propios de 220 son 1, 2, 4, 5, 10, 11, 20, 22, 44,
55 y 110. Si sumamos estos números, obtenemos 284, que es el segundo número del par. Por otro lado,
los divisores propios de 284 son 1, 2, 4, 71 y 142, y si los sumamos, obtenemos 220, que es el primer
número del par.
'''

primero_num = int(input('Digite el primer numero: '))
segundo_num = int(input('Digite el segundo numero: '))
sum_primer_num = 0
sum_segundo_num = 0
for i in range(1, primero_num):
    if primero_num % i == 0:
        sum_primer_num += i

for j in range(1, segundo_num):
    if segundo_num % j == 0:
        sum_segundo_num += j
print('-' * 40)
if sum_primer_num == segundo_num:
    if sum_segundo_num == primero_num:
        print(f'Los numeros {primero_num} y {segundo_num} son amigos ')
else:
    print(f'Los numeros {primero_num} y {segundo_num} !No son amigos¡ ')

print('-' * 40)
