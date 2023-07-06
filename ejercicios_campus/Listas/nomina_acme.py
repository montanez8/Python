empleados = []

def validar_id(id , empleados):
    for empleado in empleados:
        if empleado[0] == id:
            return False
    return True
def agregar_empleado(empleados):
    try:
        id = int(input("Ingrese el ID del empleado: "))
    except ValueError:
        print("\n!Error! .Ingrese un ID valido \n")
    nombre = input("Ingrese el nombre del empleado: ")
    horas = int(input("Ingrese las horas trabajadas por el empleado: "))
    valor_hora = int(input("Ingrese el valor de la hora trabajada: "))
    if validar_id(id , empleados):
        empleados.append([id, nombre, horas, valor_hora])
        print("Empleado Creado exitosamente. ")
    else:
        print("-"*16,"Advertencia:" ,"-"*16,"\nEl ID ya existe. No se puede insertar el empleado.\n")

def modificar_empleado(empleados):
    
    id = input("Ingrese el ID del empleado a modificar: ")
    for empleado in empleados:
        if empleado[0] == id:
            nombre = input("Ingrese el nuevo nombre del empleado: ")
            horas = int(input("Ingrese las nuevas horas trabajadas por el empleado: "))
            valor_hora = int(input("Ingrese el nuevo valor de la hora trabajada: "))
            empleado[1] = nombre
            empleado[2] = horas
            empleado[3] = valor_hora
            return
    print("Empleado no encontrado")

def buscar_empleado(empleados):
    id = int(input("Ingrese el ID del empleado a buscar: "))
    for empleado in empleados:
        if empleado[0] == id:
            print("-"*15,"Empleado Encontrado" ,"-"*15)
            print("ID: ", empleado[0])
            print("Nombre: ", empleado[1])
            print("Horas trabajadas: ", empleado[2])
            print("Valor de la hora trabajada: ", format(empleado[3], ",") , "\n")
            return
    print("Empleado no encontrado")

def eliminar_empleado(empleados):
    id = int(input("Ingrese el ID del empleado a eliminar: "))
    for empleado in empleados:
        if empleado[0] == id:
            empleados.remove(empleado)
            print("-"*15 , "Eliminando Empleado", "-"*15)
            print("Empleado eliminado \n")
            return
    print("Empleado no encontrado \n")

def listar_empleados(empleados):
    for i in range(len(empleados)):
        if i % 5 == 0 and i != 0:
            opcion = input("¿Desea seguir viendo? (s/n): ")
            if opcion.lower() != "s":
                return
        print("-"*15,"Listado de empleados","-"*15)
        print("ID: ", empleados[i][0])
        print("Nombre: ", empleados[i][1])
        print("Horas trabajadas: ", empleados[i][2])
        print("Valor de la hora trabajada: ", format(empleados[i][3]),",")
        print("-"*30 , "\n")

def listar_nomina(empleados):
    id = int(input("Ingrese el ID del empleado a listar nómina: "))
    for empleado in empleados:
        if empleado[0] == id:
            print("-"*15 , "Nomina Empleado" , "-"*15)
            print("Nómina: ", format(empleado[2] * empleado[3],","),"\n")
            return
    print("Empleado no encontrado\n")

def listar_nomina_todos(empleados):
    print("-"*15,"Nomina Empleados","-"*15)
    for empleado in empleados:
        nomina = empleado[2] * empleado[3]
        print(f"El empleado {empleado[1]} tiene una nomina por valor de:", format(nomina,","))
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
        print("Hasta Luego...")
        break
    else:
        print("Opción inválida")
