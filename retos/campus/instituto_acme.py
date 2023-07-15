import json
import io

def menu():
    while True:
        print("*** INSTITUTO ACME ***")
        print("MENU")
        print("1- Estudiantes")
        print("2- Notas")
        print("3- Reportes")
        print("4- Salir")
        opcion = int(input("Escoja una opción (1-4): "))
        if opcion == 1:
            estudiantes()
        elif opcion == 2:
            notas()
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


def estudiantes():
    menu_stud()
def registro_estud(estudiantes):
    try:
        id = int(input("Ingrese el id del estudiante: "))
    except ValueError:
        print("!Error ! .Ingrese un id valido")
    nombre = input("Ingrese el nombre del estudiante: ")
    while True:
        genero = input(
            "Genero del estudiante (Femenino,Masculino").capitalize()
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
    if validar_id(id, estudiantes):
        estudiantes[id] = {"nombre": nombre, "genero": genero, "grado": grado}
        print("Estudiante creado con exito")
        with open('estudiantes.json', 'w') as estd:
            json.dump(estudiantes, estd, indent=4)
    return estudiantes


def modificar_estd(estudiantes):
    id = int(input("Ingrese el Id del estudiante a modificar: "))
    if id in estudiantes:
        nombre = input("Ingrese el nuevo nombre del estudiante: ")
        while True:
            genero = input(
                "Genero del estudiante (Femenino,Masculino").capitalize()
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
        with open(estudiantes.json, "w") as estd:
            json.dump(estudiantes, estd, indent=4)
    else:
        print("Estudiante no encontrado")


def buscar_estd(estudiantes):
    id = int(input("Ingrese el Id del estudiante a buscar: "))
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


def eliminar_estd():
    pass


def validar_id(id, estudiantes):
    return id not in estudiantes


def cargar_estudiantes():
    try:
        estudiantes = {}
        with open('estudiantes.json', 'a+') as estd:
            estudiantes = estd.json.load(estd)
            return estudiantes
    except FileNotFoundError:
        estudiantes = {}
        return estudiantes


def notas():
    pass


def reportes():
    pass


def continuar():
    input('Ingrese cualquier tecla para continuar')


def guardar_archivo(estudiantes):
    with open('estudiantes.json', 'w') as f:
        json.dump(estudiantes, f)


menu()
