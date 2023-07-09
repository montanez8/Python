
def factorial(numero):
    factorial = 1
    for i in range(1 , numero+ 1):
        factorial = factorial * i
    return format(factorial,',')

numero = int(input("Digite un numero para sacar su factorial: "))
print(factorial(numero))