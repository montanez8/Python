import json


def cargar_datos():
    try:
        with open('datos.json', 'r') as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        datos = {}
    return datos


def guardar_datos(datos):
    with open('datos.json', 'w') as archivo:
        json.dump(datos, archivo)


def ingresar_estudiante(datos):
    while True:
        id_estudiante = int(input("Ingrese el id del estudiante: "))
        for grado, estudiantes in datos.items():
            if id_estudiante in estudiantes:
                print("El id del estudiante ya existe.")
                ingresar_estudiante(datos)
        break
    nombre_estudiante = input("Ingrese el nombre del estudiante: ")
    sexo_estudiante = input("Ingrese el sexo del estudiante (M/F): ").upper()
    if sexo_estudiante not in ["M", "F"]:
        print("El sexo del estudiante debe ser M o F.")
        return
    grado_estudiante = input("Ingrese el grado del estudiante: ")
    if grado_estudiante not in datos:
        datos[grado_estudiante] = {}
    datos[grado_estudiante][int(id_estudiante)] = {
        "nombre": nombre_estudiante, "sexo": sexo_estudiante}
    guardar_datos(datos)
    print("El estudiante ha sido registrado exitosamente.")


def modificar_estudiante(datos):
    id_estudiante = input("Ingrese el id del estudiante que desea modificar: ")
    encontrado = False
    for grado, estudiantes in datos.items():
        if id_estudiante in estudiantes:
            encontrado = True
            nombre_estudiante = input(
                "Ingrese el nuevo nombre del estudiante: ")
            sexo_estudiante = input(
                "Ingrese el nuevo sexo del estudiante (M/F): ").upper()
            if sexo_estudiante not in ["M", "F"]:
                print("El sexo del estudiante debe ser M o F.")
                return
            estudiantes[id_estudiante]["nombre"] = nombre_estudiante
            estudiantes[id_estudiante]["sexo"] = sexo_estudiante
            guardar_datos(datos)
            print("El estudiante ha sido modificado exitosamente.")
            break
    if not encontrado:
        print("El id del estudiante no existe.")


def buscar_estudiante(datos):
    datos = cargar_datos()
    id_estudiante = input("Ingrese el id del estudiante que desea buscar: ")
    encontrado = False
    for grado, estudiantes in datos.items():
        if id_estudiante in estudiantes:
            encontrado = True
            print()
            print(f"Los datos del estudiante con id: {id_estudiante} son:\n")
            print(f"Nombre: {estudiantes[id_estudiante]['nombre']}")
            print(f"Sexo: {estudiantes[id_estudiante]['sexo']}\n")

            break
    if not encontrado:
        print("El id del estudiante no existe.")


def eliminar_estudiante(datos):
    id_estudiante = input("Ingrese el id del estudiante que desea eliminar: ")
    encontrado = False
    for grado, estudiantes in datos.items():
        if id_estudiante in estudiantes:
            encontrado = True
            del estudiantes[id_estudiante]
            guardar_datos(datos)
            print("El estudiante ha sido eliminado exitosamente.")
            break
    if not encontrado:
        print("El id del estudiante no existe")


def ingresar_notas(datos):
    grupo = input("Ingrese el grupo al cual desea ingresar notas: ")
    if grupo not in datos:
        confirmacion_str = input(
            f"No hay estudiantes registrados en el grupo {grupo}. ¿Desea crear un nuevo grupo? (S/N): ")
        if confirmacion_str.upper() == "S":
            datos[grupo] = {}
        else:
            return
    estudiantes_grupo = sorted(
        datos[grupo].items(), key=lambda x: x[1]["nombre"])
    for id_est, info in estudiantes_grupo:
        notas = []
        while True:
            nota_str = input(
                f"Ingrese la nota para {info['nombre']} (o presione enter para terminar): ")
            if nota_str == "":
                break
            try:
                nota_float = float(nota_str)
                notas.append(nota_float)
            except ValueError:
                print("La nota debe ser un número.")
                continue
        info["notas"] = notas
    guardar_datos(datos)
    print(f"Notas ingresadas exitosamente para el grupo {grupo}.")


def continuar():
    input('Ingrese cualquier tecla para continuar')


def reporte_notas_promedio(datos):
    print("-"*15, "Reporte Notas Promedio", '-'*15)
    for grado, estudiantes in datos.items():
        notas_grado = []
        for estudiante in estudiantes.values():
            notas_grado.extend(estudiante.get("notas", []))
        if notas_grado:
            promedio_grado = sum(notas_grado) / len(notas_grado)

            print(f"Grado {grado}: {promedio_grado:.2f}")
        else:
            print(f"No hay notas registradas para el grado {grado}.")


def reporte_terna_excelencia(datos):
    print("-"*15, "Reporte Terna Exelencia", '-'*15)
    for grado, estudiantes in datos.items():
        notas_estudiantes = []
        for id_estudiante, info in estudiantes.items():
            notas_estudiante = info.get("notas", [])
            if notas_estudiante:
                promedio_estudiante = sum(
                    notas_estudiante) / len(notas_estudiante)
                notas_estudiantes.append(
                    (id_estudiante, info["nombre"], promedio_estudiante))
        if notas_estudiantes:
            print(f"Terna de excelencia para el grado {grado}:")
            for id_estudiante, nombre, promedio in sorted(notas_estudiantes, key=lambda x: x[2], reverse=True)[:3]:
                print(f"{nombre} ({id_estudiante}): {promedio:.2f}")
        else:
            print(f"No hay notas registradas para el grado {grado}.")


def reporte_terna_excelencia_colegio(datos):
    notas_estudiantes = []
    for estudiantes in datos.values():
        for id_estudiante, info in estudiantes.items():
            notas_estudiante = info.get("notas", [])
            if notas_estudiante:
                promedio_estudiante = sum(
                    notas_estudiante) / len(notas_estudiante)
                notas_estudiantes.append(
                    (id_estudiante, info["nombre"], info["grado"], promedio_estudiante))
    if notas_estudiantes:
        print("Terna de excelencia del colegio:")
        for id_estudiante, nombre, grado, promedio in sorted(notas_estudiantes, key=lambda x: x[3], reverse=True)[:3]:
            print(f"{nombre} ({id_estudiante}), Grado {grado}: {promedio:.2f}")
    else:
        print("No hay notas registradas en el colegio.")


def menu_reportes():
    while True:
        opcion = int(input(
            "1.reporte notas promedio\n2.reporte terna excelencia\n3.reporte terna excelencia colegio\n: "))
        datos = cargar_datos()
        print(opcion)
        if opcion in [1, 2, 3]:
            if opcion == 1:
                reporte_notas_promedio(datos)
                continuar()
            if opcion == 2:
                reporte_terna_excelencia(datos)
                continuar()
            if opcion == 3:
                reporte_terna_excelencia_colegio(datos)
                continuar()
        else:
            print("Opcion no valida")
            continue


def mostrar_menu():
    datos = cargar_datos()
    print("\nBienvenido al programa de registro e informe de notas de los estudiantes.")
    while True:
        print("\nMenú:")
        print("1. Ingresar un nuevo estudiante.")
        print("2. Modificar un estudiante existente.")
        print("3. Buscar un estudiante.")
        print("4. Eliminar un estudiante.")
        print("5. Ingresar notas de un grupo.")
        print("6. Reportes")
        print("7. Salir del programa.")
        opcion_str = input(
            "\nIngrese el número de la opción que desea ejecutar: ")
        try:
            opcion_int = int(opcion_str)
        except ValueError:
            print("La opción debe ser un número.")
            continue
        if opcion_int == 1:
            ingresar_estudiante(datos)
            continuar()
        elif opcion_int == 2:
            modificar_estudiante(datos)
            continuar()
        elif opcion_int == 3:
            buscar_estudiante(datos)
            continuar()
        elif opcion_int == 4:
            eliminar_estudiante(datos)
        elif opcion_int == 5:
            ingresar_notas(datos)
            continuar()
        elif opcion_int == 6:
            menu_reportes()
        elif opcion_int == 7:
            print("Hasta Luego..")
            break
        else:
            print("La opción ingresada no es válida.")
            continuar()


mostrar_menu()
