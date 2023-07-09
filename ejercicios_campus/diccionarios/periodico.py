def verificar_entero(mensaje):
    while True:
        print("\n", "-" * 60)
        try:
            numero = int(input(mensaje))
            if numero < 1 or numero > 3:
                print("Digita una opción válida")
                continue
            return numero
        except ValueError:
            print("Error, ingrese un valor válido")

def imprimir_resultado(resultado, mensaje):
    print(f"\n{len(resultado)} compraron el periódico {mensaje}")
    print("\n¿Quieres ver los códigos de los estudiantes?")
    print("1. Sí")
    print("2. No")
    s_opcion = verificar_entero("Digita la opción: ")
    if s_opcion == 1:
        print("".join(str(resultado)))
    print("\nVolverás al menú principal")

ingles = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
frances = set([10, 1, 2, 3, 11, 21, 55, 6, 8])
while True:
    print("\nEstudiantes que compraron:")
    print(f"El periódico Inglés: {len(ingles)}")
    print(f"El periódico Francés: {len(frances)}")
    print("\nQuieres ver los estudiantes que compraron: ")
    print("1. Solo el periódico Inglés")
    print("2. Solo el periódico Francés")
    print("3. Salir")
    opcion = verificar_entero("Digita la opción: ")
    if opcion == 1:
        resultado = ingles - frances
        imprimir_resultado(resultado, "Inglés")
    elif opcion == 2:
        resultado = frances - ingles
        imprimir_resultado(resultado, "Francés")
    else:
        print("Hasta Luego..")
        break
