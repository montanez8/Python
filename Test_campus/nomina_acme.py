empleados = {}
def validar_id(id, empleados):
    return id not in empleados  
def agregar_empleado(empleados):
    while True:
        try:
            id = int(input("Ingrese el ID del empleado: "))
        except ValueError:
            print("\n!Error! .Ingrese un ID valido \n")
    nombre = input("Ingrese el nombre del empleado: ")
    while True:
        horas = int(input("Ingrese las horas trabajadas por el empleado: "))
        if horas <= 160:
            horas = horas
            break
        else:
            print("Numero de horas tiene que ser menor a 160")
            continue
    while True:
        valor_hora = int(input("Ingrese el valor de la hora trabajada: "))
        if valor_hora >= 8000 and valor_hora <= 150000:
            valor_hora = valor_hora
            print("estoy aca valor hora")
            break
        else:
            print("Valor hora fuera de rango (8000-150000)")
            continue
    if validar_id(id, empleados):
        empleados[id] = {'nombre': nombre,'horas': horas, 'valor_hora': valor_hora}
        print("Empleado Creado exitosamente. ")
    else:
        print("-"*16, "Advertencia:", "-"*16,"\nEl ID ya existe. No se puede insertar el empleado.\n")

def modificar_empleado(empleados):
    id = int(input("Ingrese el ID del empleado a modificar: "))
    if id in empleados:
        nombre = input("Ingrese el nuevo nombre del empleado: ")
        horas = int(
            input("Ingrese las nuevas horas trabajadas por el empleado: "))
        valor_hora = int(
            input("Ingrese el nuevo valor de la hora trabajada: "))
        empleados[id]['nombre'] = nombre
        empleados[id]['horas'] = horas
        empleados[id]['valor_hora'] = valor_hora
    else:
        print("Empleado no encontrado")


def buscar_empleado(empleados):
    id = int(input("Ingrese el ID del empleado a buscar: "))
    if id in empleados:
        empleado = empleados[id]
        print("-"*15, "Empleado Encontrado", "-"*15)
        print("ID: ", empleado['id'])
        print("Nombre: ", empleado['nombre'])
        print("Horas trabajadas: ", empleado['horas'])
        print("Valor de la hora trabajada: ", format(
            empleado['valor_hora'], ","), "\n")
    else:
        print("Empleado no encontrado")


def eliminar_empleado(empleados):
    id = int(input("Ingrese el ID del empleado a eliminar: "))
    if id in empleados:
        del empleados[id]
        print("-"*15, "Eliminando Empleado", "-"*15)
        print("Empleado eliminado \n")
    else:
        print("Empleado no encontrado \n")


def listar_empleados(empleados):
    for i, (id, empleado) in enumerate(empleados.items()):
        if i % 5 == 0 and i != 0:
            opcion = input("¿Desea seguir viendo? (s/n): ")
            if opcion.lower() != "s":
                return
        print("-"*15, "Listado de empleados", "-"*15)
        print("ID: ", empleado['id'])
        print("Nombre: ", empleado['nombre'])
        print("Horas trabajadas: ", empleado['horas'])
        print("Valor de la hora trabajada: ",format(empleado['valor_hora']), ",")
        print("-"*30, "\n")


def listar_nomina(empleados):
    id = int(input("Ingrese el ID del empleado a listar nómina: "))
    if id in empleados:
        empleado = empleados[id]
        nomina = empleado['horas'] * empleado['valor_hora']
        print("-"*15, "Nomina Empleado", "-"*15)
        print("Nómina: ", format(nomina, ","), "\n")
    else:
        print("Empleado no encontrado\n")


def listar_nomina_todos(empleados):
    print("-"*15, "Nomina Empleados", "-"*15)
    for id, empleado in empleados.items():
        nomina = empleado['horas'] * empleado['valor_hora']
        print(f"El empleado {empleado['nombre']} tiene una nomina por valor de:", format(
            nomina, ","))
    print("\n")


while True:
    print("*** NOMINA ACME ***")
    print("MENU")
    print("1- Agregar empleado")
    print("2- Modificar empleado")
    print("3- Buscar empleado")
    print("4- Eliminar empleado")
    print("5- Listar empleados")
    print("6- Listar nómina de un empleado")
    print("7- Listar nómina de todos los empleados")
    print("8- Salir")
    opcion = int(input("Escoja una opción (1-8): "))
    if opcion == 1:
        agregar_empleado(empleados)
        print(empleados)
    elif opcion == 2:
        modificar_empleado(empleados)
    elif opcion == 3:
        buscar_empleado(empleados)
    elif opcion == 4:
        eliminar_empleado(empleados)
    elif opcion == 5:
        listar_empleados(empleados)
    elif opcion == 6:
        listar_nomina(empleados)
    elif opcion == 7:
        listar_nomina_todos(empleados)
    elif opcion == 8:
        break
