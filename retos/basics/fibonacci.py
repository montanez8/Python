# numero = int(input("Ingrese el numero: "))//2
# temp = 0
# temp2 =1
# for i in range(0 , numero ):
#     print(temp , temp2 ,end=",")
#     temp = temp + temp2 #2
#     temp2 = temp2 + temp

# num = int(input("¿Cuántos términos? "))

# n1, n2 = 0, 1
# count = 0

# if num <= 0:
#     print("Por favor, ingrese un número entero positivo")
# elif num == 1:
#     print("Secuencia de Fibonacci hasta", num, ":")
#     print(n1)
# else:
#     print("Secuencia de Fibonacci:")
#     for i in range(num):
#         print(n1,end=",")
#         nth = n1 + n2
#         n1 = n2
#         n2 = nth


# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return(fibonacci(n-1) + fibonacci(n-2))

# nterms = int(input("¿Cuántos términos? "))

# if nterms <= 0:
#     print("Por favor, ingrese un número entero positivo")
# else:
#     print("Secuencia de Fibonacci:")
#     for i in range(nterms):
#         print(fibonacci(i))


nterms = int(input("¿Cuántos términos? "))
n1, n2 = 0, 1
count = 0

if nterms <= 0:
    print("Por favor, ingrese un número entero positivo")
elif nterms == 1:
    print("Secuencia de Fibonacci hasta", nterms, ":")
    print(n1)
else:
    print("Secuencia de Fibonacci:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
