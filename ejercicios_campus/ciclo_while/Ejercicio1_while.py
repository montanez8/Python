# Construya un programa que verifique si un número dado es perfecto. Un número perfecto es un
# número entero positivo que es igual a la suma de sus divisores propios positivos (excluyendo el
# número mismo). En otras palabras, si sumas todos los divisores propios de un número perfecto, el
# resultado será igual al número original.
# Por ejemplo, el número 6 es considerado un número perfecto. Sus divisores propios son 1, 2 y 3. Si
# sumamos estos números: 1 + 2 + 3 = 6, obtenemos el mismo número original.
#

numero = int(input('Ingrese un numero entero positivo: '))
i = 1
sum_div = 0
while i <= numero:
    if numero % i == 0:
        sum_div += i
        if sum_div == numero:
            print('El numero es Perfecto')
