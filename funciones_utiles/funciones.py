# leer un numero entero
def leerInt(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 1:
                print("Error! El codigo debe ser entero postivo.")
                input("Digite cualquier tecla para continuar...")
                continue
            return n
        except ValueError:
            print("Error! Ingrese un numero valido")


# validar numero entero
def validar_entero(numero):
    try:
        int(numero)
        return True
    except ValueError:
        return False


def msgError(msg):
    print("----> ¡ERROR!" + msg)
    input("---> Presione ENTER para continuar")

# funcion menu


def menu():
    while True:
        print("1. Opción 1")
        print("2. Opción 2")
        print("3. Opción 3")
        print("4. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":

            pass
        elif opcion == "2":

            pass
        elif opcion == "3":

            pass
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Intente de nuevo.")


# guardar diccionario en json
import json
def guardar_archivo(diccionario, ruta):
    with open(ruta, "w") as archivo:
        json.dump(diccionario, archivo)
