import json
import io
        
# funcion que retorna el tipo de tarjeta
def tipo_tarjeta():
    while  True:
        op = int(input("Seleccione segun el tipo de tarjeta.\n1.Master Card\n2.Visa\n3.American Express\n--> "))
        tipo = None
        if op in [1,2,3]:
            if op == 1:
                tipo = "Master Card"
            elif op == 2:
                tipo = "Visa"
            else:
                tipo = "American Express"
        else:
            print("Opcion no valida")
            continue
        break
    return tipo

def continuar():
    input('Ingrese cualquier tecla para continuar')      
# funcion que permite la gestion de las tarjetas de credito (añadir , eliminar , modificar)
def  tarjetas_credito():
    tarjetas = cargar_tarjetas("tarjetas.json")
    clientes = cargar_clientes("clientes.json")
    ruta = "Prueba 1/archivosPersistentes/tarjetas.json"
    while True:
        print("-"*45)
        print("\nGestion de tarjetas de credito acme\n")
        opcion = input("Seleccione que desea hacer\n1.Agregar Tarjeta\n2.Modificar Tarjeta\n3.Eliminar Tarjeta\n4.Salir\n--> ")
        if opcion == "1":
            agregar_tarjeta(tarjetas,clientes,ruta)
            continuar()
        elif opcion == "2":
            modificar_tarjeta(tarjetas,clientes,ruta)
            continuar()
        elif opcion == "3":
            eliminar_tarjeta(tarjetas,ruta)
            continuar()
        elif opcion == "4":
            print("Hasta Luego")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
            continue
        
def guardar_tarjeta(ruta,datos):
    with open(ruta, 'w') as archivo:
        json.dump(datos, archivo)
        
# funcion que permite agregar una tarjeta de un cliente
def agregar_tarjeta(tarjetas , clientes , ruta):
    while True:
        tipo = tipo_tarjeta()
        while True:
            num_tarjeta = input("Ingrese el numero de la tarjeta de credito (16 digitos): ")
            if len(num_tarjeta) ==16:
                num_tarjeta = num_tarjeta
                break
            else:
                print("!Error ! El numero de la tarjeta tiene que tener 16 digitos")
        while True:
            mes = int(input("Ingrese el mes validez tarjeta .valor numerico : "))
            if mes >=1 and mes <=12:
                mes = mes
                break
            print("Mes no valido")
            continue
        while True:
            agno = int(input("Ingrese el año validez tarjeta .Mayor al año actual :  "))
            if agno >= 2023:
                agno = agno
                break
            print("Año no valido tiene que ser mayor al año actual")
            continue
        while True:
            cod = int(input("Ingrese el codigo verificacion .(100-999) :  "))
            if cod >= 100 and cod <=999:
                cod = cod
                break
            print("El codigo de verificacion tiene que estar en el rango (100-999)")
            continue
        while True:
            id_cliente = input("Ingrese el Id del cliente a asignar tarjeta: ")
            if id_cliente in clientes:
                id_cliente = id_cliente
                break
            else:
                print(f"El id {id_cliente} No esta registrado")
                continue
        validez = f"{mes}/{agno}"
        tarjetas[num_tarjeta] = {}
        tarjetas[num_tarjeta][tipo]={"Validez":validez ,"codigo verificacion":cod ,"cliente":id_cliente}
        guardar_tarjeta(ruta,tarjetas)
        print()
        print("-"*15,"Creando Tarjeta","-"*15)
        print("-"*12,"Tarjeta Creada con exito","-"*12)
        break
# funcion que permite modificar una tarjeta existente
def modificar_tarjeta(tarjetas , clientes , ruta):
    num_tarjeta = input("Ingrese el numero de tarjeta a modificar: ")
    if num_tarjeta in tarjetas:
        tipo = tipo_tarjeta()
        while True:
            mes = int(input("Ingrese el mes validez tarjeta .valor numerico : "))
            if mes >=1 and mes <=12:
                mes = mes
                break
            print("Mes no valido")
            continue
        while True:
            agno = int(input("Ingrese el año validez tarjeta .Mayor al año actual :  "))
            if agno >= 2023:
                agno = agno
                break
            print("Año no valido tiene que ser mayor al año actual")
            continue
        while True:
            cod = int(input("Ingrese el codigo verificacion .(100-999) :  "))
            if cod >= 100 and cod <=999:
                cod = cod
                break
            print("El codigo de verificacion tiene que estar en el rango (100-999)")
            continue
        while True:
            id_cliente = input("Ingrese el Id del cliente a asignar tarjeta: ")
            if id_cliente in clientes:
                id_cliente = id_cliente
                break
            else:
                print(f"El id {id_cliente} No esta registrado")
                continue
        validez = f"{mes}/{agno}"
        tarjetas[num_tarjeta] = {}
        tarjetas[num_tarjeta][tipo]={"Validez":validez ,"codigo verificacion":cod ,"cliente":id_cliente}
        guardar_tarjeta(ruta,tarjetas)
        print()
        print("-"*15,"Modificando Tarjeta","-"*15)
        print("-"*12,"Tarjeta Moficada con exito","-"*12)

# funcion que permite eliminar una tarjeta existente
def eliminar_tarjeta(tarjetas,ruta):
    num_tarjeta = input("Ingrese el numero de tarjeta a eliminar: ")
    if num_tarjeta in tarjetas:
        del tarjetas[num_tarjeta]
        guardar_cliente(ruta,tarjetas)
        print("-"*15, "Eliminando Tarjeta", "-"*15)
        print("Tarjeta eliminada exitosamente")

def guardar_cliente(ruta,datos):
    with open(ruta, 'w') as archivo:
        json.dump(datos, archivo)
# funcion que permite la gestion de los clientes (añadir , eliminar , modificar)
def clientes():
    clientes = cargar_clientes("clientes.json")
    while True:
        print("-"*45)
        print("\nGestion de clientes acme\n")
        opcion = input("Seleccione que desea hacer\n1.Agregar Cliente\n2.Modificar Cliente\n3.Eliminar Cliente\n--> ")
        if opcion == "1":
            agregar_cliente(clientes)
            continuar()
        elif opcion == "2":
            modificar_cliente(clientes)
            continuar()
        elif opcion == "3":
            eliminar_cliente(clientes)
            continuar()
        elif opcion == "4":
            print("Hasta Luego")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
            continue
        
# funcion que permite agregar un nuevo  cliente
def agregar_cliente(clientes):
    ruta = "clientes.json"
    while True:
        try:  
            nombre = input("Nombre cliente: ")
        except ValueError:
            print("!Error! .Nombre incorrecto")
            continue
        while True:
            cedula = input("Ingrese cedula cliente: ")
            if cedula in clientes:
                print("Cliente ya registrado.")
                continue
            else:
                cedula = cedula
                break
        telefono = (input("Telefono: "))
        if len(telefono) <= 10:
            telefono = telefono
        else:
            print("Telefono debe tener 6 digitos")
            continue
        genero = input(
                "Ingrese el sexo del cliente (M/F): ").upper()
        if genero not in ["M", "F"]:
                print("El sexo del estudiante debe ser M o F.")
                
        clientes[cedula]= {"nombre":nombre , "telefono":telefono , "sexo": genero}
        guardar_cliente(ruta,clientes)
        print("Cliente Creado Exitosamente")
        break 
# funcion que permite modificar informacion de un cliente existente
def modificar_cliente(clientes):
    ruta = "clientes.json"
    cedula = (input("Ingrese cedula cliente: "))
    if cedula in clientes:
        while True:
            nombre = input("Digite el nuevo nombre cliente: ")
            telefono = (input("Telefono: "))
            if len(telefono) <= 10:
                telefono = telefono
            else:
                print("Telefono debe tener 6 digitos")
                continue 
            genero = input(
                    "Ingrese el sexo del cliente (M/F): ").upper()
            if genero not in ["M", "F"]:
                    print("El sexo del estudiante debe ser M o F.")
            clientes[cedula]= {"nombre":nombre , "telefono":telefono , "sexo": genero}
            guardar_cliente(ruta,clientes)
            print("Cliente Modificado Exitosamente")
            break 
    else:
        print(f"El cliente con cedula {cedula} .No esta Registrado ")
            
# funcion que permite eliminar un cliente existente.
def eliminar_cliente(clientes):
    ruta = "clientes.json"
    cedula = (input("Ingrese cedula cliente: "))
    if cedula in clientes:
        del clientes[cedula]
        print("-"*15, "Eliminando Cliente", "-"*15)
        print("Cliente eliminado exitosamente")
        guardar_cliente(ruta,clientes)
    else:
        print("Cliente no registrado")

def  tarjetas_cliente(tarjetas , clientes):
    for keys , tarjeta in tarjetas.items():
        for key , info in tarjeta.items():
            tipo = key
            validez = info["Validez"]
            cod = info["codigo verificacion"]
            cliente = info["cliente"]
            id_cliente = input("Digite el id del cliente a verificar informacion de sus tarjetas. :")
            if cliente == id_cliente:
                print("{:<20} {:<10} {:<10} {:<20}".format("Tipo Tarjeta", "Validez", "Codigo Verificacion", "Cliente"))
                print("-" * 70)
                print("{:<20} {:<10} {:<10} {:<10}".format(tipo ,validez ,cod ,cliente ))
                print("-"*70)
                if id_cliente in clientes:
                    for id , client in clientes.items():
                        if id == cliente:
                            print("{:<20} {:<10} {:<10}".format("Nombre", "Telefono", "Sexo"))
                            print("-" * 70)
                            nombre = client["nombre"]
                            tel = client["telefono"]
                            sexo = client["sexo"]
                            print("{:<20} {:<10} {:<10}".format(nombre , tel , sexo))
                            print("-" * 70)
                            break
        print("-" * 70)
        

def info_tarjeta(tarjetas,clientes):
    num_tarjeta = input("Ingrese el numero de tarjeta a verificar Informacion: ")
    print("{:<20} {:<10} {:<10} {:<20}".format("Tipo Tarjeta", "Validez", "Codigo Verificacion", "Cliente"))
    print("-" * 70)
    if num_tarjeta in tarjetas:
        print()
        print(f"Informacion de La tarjeta de credito numero {num_tarjeta}")
        print()
        for keys , tarjeta in tarjetas.items():
            for key , info in tarjeta.items():
                if keys == num_tarjeta:
                    tipo = key
                    validez = info["Validez"]
                    cod = info["codigo verificacion"]
                    cliente = info["cliente"]
                    print("{:<20} {:<10} {:<10} {:<10}".format(tipo ,validez ,cod ,cliente ))
                    print("-"*70)
                    if cliente in clientes:
                        for id , client in clientes.items():
                            if id == cliente:
                                print("{:<20} {:<10} {:<10}".format("Nombre", "Telefono", "Sexo"))
                                print("-" * 70)
                                nombre = client["nombre"]
                                tel = client["telefono"]
                                sexo = client["sexo"]
                                print("{:<20} {:<10} {:<10}".format(nombre , tel , sexo))
                                print("-" * 70)
        print("-" * 70)
        
    else:
        print("Tarjeta de credito no registrada..")
    

def list_tarjetas(tarjetas):
        for keys , tarjeta in tarjetas.items():
            for key , info in tarjeta.items():
                tipo = key
                validez = info["Validez"]
                cod = info["codigo verificacion"]
                cliente = info["cliente"]
                print("{:<20} {:<10} {:<10} {:<10}".format(tipo ,validez ,cod ,cliente ))
                print("-"*70)

def list_clien_tarjetas(tarjetas , clientes):
    print("{:<20} {:<10} {:<10} {:<20}".format("Tipo Tarjeta", "Validez", "Codigo Verificacion", "Cliente"))
    print("-" * 70)
    print()
    print()
    for keys , tarjeta in tarjetas.items():
        for key , info in tarjeta.items():
            tipo = key
            validez = info["Validez"]
            cod = info["codigo verificacion"]
            cliente = info["cliente"]
            print("{:<20} {:<10} {:<10} {:<10}".format(tipo ,validez ,cod ,cliente ))
            print("-"*70)
            for id , client in clientes.items():
                if id == cliente:
                    print("{:<20} {:<10} {:<10}".format("Nombre", "Telefono", "Sexo"))
                    print("-" * 70)
                    nombre = client["nombre"]
                    tel = client["telefono"]
                    sexo = client["sexo"]
                    print("{:<20} {:<10} {:<10}".format(nombre , tel , sexo))
                    print("-" * 70)
            print("-" * 70)
def cant_tarj_tipo(tarjetas):
    tipo = tipo_tarjeta()
    for key , tarjeta in tarjetas.items():
        for keys , info in tarjeta.items():
            count = 0
            if keys == tipo:
                count +=1
                print(f"La cantidad de tarjetas de {keys} es {count}")


# funcion que permite gestionar los distintos informes requeridos
def informes():
    tarjetas = cargar_tarjetas("tarjetas.json")
    clientes = cargar_clientes("clientes.json")
    while True:
        op = input("Seleccione el informe a visualizar.\n1.Tarjetas de credito de un cliente.\n2.Informacion de una Tarjeta de Credito.\n3.Listado de tarjetas de crédito.\n4.Listado de los clientes con tarjetas de crédito.\n5.Cantidad de tarjetas de cierto tipo.\n6.Salir\n-->")
        if op == "1":
            tarjetas_cliente(tarjetas , clientes)
            continuar()
        elif op == "2":
            info_tarjeta(tarjetas , clientes)
            continuar()
        elif op== "3":
            list_tarjetas(tarjetas)
            continuar()
        elif op =="4":
            list_clien_tarjetas(tarjetas , clientes)
            continuar()
        elif op == "5":
            cant_tarj_tipo(tarjetas)
            continuar()
        elif op == "6":
            print("Hasta Luego")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
            continue
        
def menu():
    while True:
        print(" "*5," Bienvenido a su banco Acme\n")
        print("1. Gestion Tarjetas Credito")
        print("2. Gestion Clientes")
        print("3. Informes")
        print("4. Salir")

        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            tarjetas_credito()
        elif opcion == "2":
            clientes()
        elif opcion == "3":
            informes()
        elif opcion == "4":
            print("Hasta Luego")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
            continue
        
# funcion que permite cargar el archivo persistente de tarjetas de credito
def cargar_tarjetas(ruta):
    try:
        tarjetas = {}
        with open(ruta, 'r') as t:
            tarjetas = json.load(t)
            return tarjetas
    except FileNotFoundError:
        tarjetas = {}
        return tarjetas
# funcion que permite cargar el archivo persistente con la informacion de los cleintes
def cargar_clientes(ruta):
    try:
        clientes = {}
        with open(ruta, 'r') as c:
            clientes = json.load(c)
            return clientes
    except FileNotFoundError:
        clientes = {}
        return clientes

menu()

