import json

def cargar_datos():
    try:
        with open("datos.json", "r") as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        datos = {}
    return datos

def guardar_datos(datos):
    with open("datos.json", "w") as archivo:
        json.dump(datos, archivo)

def ingresar_estudiante(datos):
    while True:
        id_estudiante = input("Ingrese el id del estudiante: ")
        if not id_estudiante.isdigit():
            print("El id del estudiante debe ser un número entero.")
            continue
        if int(id_estudiante) in datos:
            print("El id del estudiante ya existe.")
            continue
        break
    nombre_estudiante = input("Ingrese el nombre del estudiante: ")
    sexo_estudiante = input("Ingrese el sexo del estudiante (M/F): ")
    if sexo_estudiante not in ["M", "F"]:
        print("El sexo del estudiante debe ser M o F.")
        return
    grado_estudiante = input("Ingrese el grado del estudiante: ")
    if grado_estudiante not in datos:
        datos[grado_estudiante] = {}
    datos[grado_estudiante][int(id_estudiante)] = {"nombre": nombre_estudiante, "sexo": sexo_estudiante}
    guardar_datos(datos)
    print("El estudiante ha sido registrado exitosamente.")

def modificar_estudiante(datos):
    id_estudiante = input("Ingrese el id del estudiante que desea modificar: ")
    if id_estudiante not in datos:
        print("El id del estudiante no existe.")
        return
    nombre_nuevo = input(f"Ingrese el nuevo nombre para el estudiante {id_estudiante}: ")
    sexo_nuevo = input(f"Ingrese el nuevo sexo para el estudiante {id_estudiante} (M/F): ")
    if sexo_nuevo not in ["M", "F"]:
        print("El sexo del estudiante debe ser M o F.")
        return
    datos[id_estudiante]["nombre"] = nombre_nuevo
    datos[id_estudiante]["sexo"] = sexo_nuevo
    guardar_datos(datos)
    print(f"El estudiante {id_estudiante} ha sido modificado exitosamente.")

def buscar_estudiante(datos):
    id_estudiante = input("Ingrese el id del estudiante que desea buscar: ")
    if id_estudiante not in datos:
        print("El id del estudiante no existe.")
        return
    print(f"Nombre: {datos[id_estudiante]['nombre']}")
    print(f"Sexo: {datos[id_estudiante]['sexo']}")
    notas = datos[id_estudiante].get("notas", [])
    if notas:
        promedio = sum(notas) / len(notas)
        print(f"Notas: {notas}")
        print(f"Promedio: {promedio:.2f}")

def eliminar_estudiante(datos):
    id_estudiante = input("Ingrese el id del estudiante que desea eliminar: ")
    if id_estudiante not in datos:
        print("El id del estudiante no existe.")
        return
    confirmacion_str = input(f"¿Está seguro de que desea eliminar al estudiante {id_estudiante}? (S/N): ")
    if confirmacion_str.upper() == "S":
        del datos[id_estudiante]
        guardar_datos(datos)
        print(f"El estudiante {id_estudiante} ha sido eliminado exitosamente.")

def ingresar_notas(datos):
    grupo = input("Ingrese el grupo al cual desea ingresar notas: ")
    if grupo not in datos:
        confirmacion_str = input(f"No hay estudiantes registrados en el grupo {grupo}. ¿Desea crear un nuevo grupo? (S/N): ")
        if confirmacion_str.upper() == "S":
            datos[grupo] = {}
        else:
            return
    estudiantes_grupo = sorted(datos[grupo].items(), key=lambda x:x[1]["nombre"])
    for id_est, info in estudiantes_grupo:
        notas = []
        while True:
            nota_str = input(f"Ingrese la nota para {info['nombre']} (o presione enter para terminar): ")
            if nota_str == "":
                break
            try:
                nota_float = float(nota_str)
                notas.append(nota_float)
            except ValueError:
                print("La nota debe ser un número.")
                continue