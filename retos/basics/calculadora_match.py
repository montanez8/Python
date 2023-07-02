def input_int(msg):
    while True:
        try:
            valor = int(input(msg))
            return valor
        except ValueError:
            print("!Eror! Ingrese un numero entero valido")


def suma():
    num1 = input_int("Digite el primer numero: ")
    num2 = input_int("Digite el segundo numero: ")
    return num1 + num2


def resta():
    num1 = input_int("Digite el primer numero: ")
    num2 = input_int("Digite el segundo numero: ")
    return num1 - num2


def multiplicacion():
    num1 = input_int("Digite el primer numero: ")
    num2 = input_int("Digite el segundo numero: ")
    return num1 * num2


def modulo():
    num1 = input_int("Digite el primer numero: ")
    num2 = input_int("Digite el segundo numero: ")
    return num1 % num2


def expo():
    num1 = input_int("Digite el primer numero: ")
    num2 = input_int("Digite el segundo numero: ")
    return num1 ** num2


def division():
    while True:
        try:
            num1 = input_int("Digite el primer numero: ")
            num2 = input_int("Digite el segundo numero: ")
            print("🔹"*20)
            print(f"El resultado de la division es: {round(num1 / num2,2)}")
            print("🔹"*20)
            continuar()
        except ZeroDivisionError:
            print("!Error! .No es posible dividir entre cero")
            continue


def continuar():
    res = input("desea realizar otra operacion\n.1= SI\n.2= NO\n-->")
    if res.upper() == "SI":
        calculadora()
    else:
        exit()


def calculadora():
    while True:
        print(" "*10 , "Calculadora\n" , " "*10)
        opcion = int(input(
            "Selecciona una de las siguientes opciones:\n1.sumar\n2.restar\n3.multiplicar\n4.division\n5.modulo\n6.exponente\n7.salir\n-->"))
        match opcion:
            case 1:
                print("-"*30, "\nEl resultado de la suma es:", suma())
                print("-"*30)
                continuar()
            case 2:
                print("-"*30, "\nEl resultado de la resta es:", resta())
                print("-"*30)
                continuar()
            case 3:
                print("-"*30,"\nEl resultado de la multiplicacion es:",multiplicacion())
                print("-"*30)
                continuar()
            case 4:
                division()
                continuar()
            case 5:
                print("-"*30, "\nEl resultado del modulo es:", modulo())
                print("-"*30)
                continuar()
            case 6:
                print("-"*30, f"\nEl resultado del modulo es:", expo())
                print("-"*30)
                continuar()
            case 7:
                print("...Hasta luego...")
                exit()
            case _:
                print("Seleccione una opcion correcta")


calculadora()
