import json
import io

def menu():
    estudiante = cargar_estudiantes()
    print(estudiante)
    while True:
        print("*** INSTITUTO ACME ***")
        print("MENU")
        print("1- Estudiantes")
        print("2- Notas")
        print("3- Reportes")
        print("4- Salir")
        opcion = int(input("Escoja una opción (1-4) : "))
        if opcion == 1:
            estudiantes()
        elif opcion == 2:
            notas(grados(estudiante))
        elif opcion == 3:
            reportes()
        elif opcion == 4:
            break


def menu_stud():
    estudiantes = cargar_estudiantes()
    while True:
        print("*** INSTITUTO ACME ***")
        print("MENU")
        print("1- Registro Estudiante")
        print("2- Modificar estudiante")
        print("3- Buscar estudiante")
        print("4- Eliminar Estudiantes")
        print("5- Salir")
        opcion = int(input("Escoja una opción (1-5): "))
        if opcion == 1:
            registro_estud(estudiantes)
        elif opcion == 2:
            modificar_estd(estudiantes)
        elif opcion == 3:
            buscar_estd(estudiantes)
        elif opcion == 4:
            eliminar_estd(estudiantes)
        elif opcion == 5:
            break

def guardar_archivo(estudiantes):
    with open('estudiantes.json', 'w') as f:
        json.dump(estudiantes, f)

def estudiantes():
    menu_stud()
def registro_estud(estudiantes):
    while True:
        try:
            id = int(input("Ingrese el id del estudiante: "))
            break
        except ValueError:
            print("!Error! .Ingrese un id valido ")
            continue
    nombre = input("Ingrese el nombre del estudiante: ")
    while True:
        genero = input(
            "Genero del estudiante (Femenino,Masculino): ").capitalize()
        if genero in ["Femenino", "Masculino"]:
            genero = genero
            break
        else:
            print("Genero No Valido (Femenino , Masculino) ")
            continue
    while True:
        grado = input(f"Grado del estudiante {nombre}: ").lower()
        if grado in ["primero", "segundo", "tercero", "cuarto", "quinto", "sexto", "septimo", "octavo", "noveno", "decimo", "once"]:
            grado = grado
            break
        else:
            print("Grado estudiante no valido ")
            continue
    if validar_id(id, estudiantes):
        estudiantes[id] = {"nombre": nombre, "genero": genero, "grado": grado}
        print("Estudiante creado con exito")
        with open('estudiantes.json', 'w') as estd:
            json.dump(estudiantes, estd, indent=4)
    else:
        print(f"El id {id} ya esta registrado")
    return estudiantes


def modificar_estd(estudiantes):
    id = (input("Ingrese el Id del estudiante a modificar: "))
    if id in estudiantes:
        nombre = input("Ingrese el nuevo nombre del estudiante: ")
        while True:
            genero = input(
                "Genero del estudiante (Femenino,Masculino): ").capitalize()
            if genero in ["Femenino", "Masculino"]:
                genero = genero
                break
            else:
                print("Genero No Valido (Femenino , Masculino)")
                continue
        while True:
            grado = input(f"Grado del estudiante {nombre}: ").lower()
            if grado in ["primero", "segundo", "tercero", "cuarto", "quinto", "sexto", "septimo", "octavo", "noveno", "decimo", "once"]:
                grado = grado
                break
            else:
                print("Grado estudiante no valido ")
                continue
        estudiantes[id] = {"nombre": nombre, "genero": genero, "grado": grado}
        with open('estudiantes.json', 'w') as estd:
            json.dump(estudiantes, estd, indent=4)
    else:
        print("Estudiante no encontrado")


def buscar_estd(estudiantes):
    id = (input("Ingrese el Id del estudiante a buscar: "))
    if id in estudiantes:
        estudiante = estudiantes[id]
        print("-"*15, "Estudiante Encontrado", "-"*15)
        print(f"""
            Nombre: {estudiante["nombre"]}
            Genero: {estudiante["genero"]}
            Grado:  {estudiante["grado"]}
        """)
    else:
        print("Estudiante no encontrado")


def eliminar_estd(estudiantes):
    id = (input("Ingrese el Id del estudiante a buscar: "))
    if id in estudiantes:
        del estudiantes[id]
        print("-"*15, "Eliminando Estudiante", "-"*15)
        print("Estudiante eliminado \n")
        with open('estudiantes.json', 'w') as estd:
            json.dump(estudiantes, estd, indent=4)
    else:
        print(f"Id: {id} no encontrado")


def validar_id(id, estudiantes):
    return id not in estudiantes


def cargar_estudiantes():
    try:
        estudiantes = {}
        with open('estudiantes.json', 'r') as estd:
            estudiantes = json.load(estd)
            return estudiantes
    except FileNotFoundError:
        estudiantes = {}
        return estudiantes
def cargar_notas():
    try:
        notas = {}
        with open('notas.json', 'r') as estd:
            notas = json.load(estd)
            return notas
    except FileNotFoundError:
        notas = {}
        return notas
    
def cargar_grados():
    try:
        grados = {}
        with open('grados.json', 'r') as grado:
            grados = json.load(grado)
            return grados
    except FileNotFoundError:
        grados = {}
        return grados
    
def grados(estudiantes):
    grados = cargar_grados()
    for key , estudiante in estudiantes.items():
        grado = estudiante["grado"]
        grados_acme = {key:{"nombre":estudiante["nombre"]}}
        for k , v in grados_acme.items():
            grados =grados[grado]={k:{"nombre":v["nombre"]}}
            print(grados)
        with open('grados.json', 'w') as grado:
                json.dump(grados, grado)
    print(grados)
    return grados

def notas(grados):
    notas = cargar_notas
    s_grado = input(" A que grado va a asignar notas: ")
    for key , grado in grados.items():
        if key == s_grado:
            nota = {key:grado}
            for k , ets in grado.items():
                notas_sts = []
                while True:
                    nota_sts = int(input("ingrese la nota del estudiante"))
                    if nota_sts !=0:
                        notas_sts.append(nota_sts)
                        print(notas_sts)
                    else:
                        break
                add_notas = {"notas":notas_sts}
                grado[k].update(add_notas)
                notas = nota
                print(notas)
            with open('notas.json', 'a') as nota:
                    json.dump(notas, nota, indent=4)
    
def reportes():
    pass


def continuar():
    input('Ingrese cualquier tecla para continuar')


menu()

