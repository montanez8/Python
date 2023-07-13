import os
def validar_id(id , empleados):
    for empleado in empleados:
        if empleado[0] == id:
            return False
    return True
def leer_archivo():
    empleados = []
    if os.path.exists('Python/ejercicios_campus/archivos/emplacme.dat'):
        with open('Python/ejercicios_campus/archivos/emplacme.dat', 'r') as f:
            next(f)
            for line in f:
                id, nombre, horas_trabajadas, valor_hora = line.strip().split(';')
                empleados.append({
                    'id': id,
                    'nombre': nombre,
                    'horas_trabajadas': int(horas_trabajadas),
                    'valor_hora': int(valor_hora)
                })
    return empleados

def guardar_archivo(empleados):
    with open('emplacme.dat', 'w') as f:
        f.write('ID;NOMBRE;HORASTRAB;VALHORA\n')
        for empleado in empleados:
            f.write(f"{empleado['id']};{empleado['nombre']};{empleado['horas_trabajadas']};{empleado['valor_hora']}\n")

def agregar_empleado(empleados):
    while True:
        id = input('Ingrese el ID del empleado: ')
        if validar_id(id , empleados):
            continue
        break
    nombre = input('Ingrese el nombre del empleado: ')
    horas_trabajadas = int(input('Ingrese las horas trabajadas por el empleado: '))
    valor_hora = int(input('Ingrese el valor de la hora trabajada por el empleado: '))
    empleados.append({
        'id': id,
        'nombre': nombre,
        'horas_trabajadas': horas_trabajadas,
        'valor_hora': valor_hora
    })
    guardar_archivo(empleados)

def modificar_empleado(empleados):
    id = input('Ingrese el ID del empleado a modificar: ')
    empleado = next((e for e in empleados if e['id'] == id), None)
    if empleado:
        nombre = input('Ingrese el nuevo nombre del empleado: ')
        horas_trabajadas = int(input('Ingrese las nuevas horas trabajadas por el empleado: '))
        valor_hora = int(input('Ingrese el nuevo valor de la hora trabajada por el empleado: '))
        empleado['nombre'] = nombre
        empleado['horas_trabajadas'] = horas_trabajadas
        empleado['valor_hora'] = valor_hora
        guardar_archivo(empleados)
    else:
        print('Empleado no encontrado')

def buscar_empleado(empleados):
    id = input('Ingrese el ID del empleado a buscar: ')
    empleado = next((e for e in empleados if e['id'] == id), None)
    if empleado:
        print(f"ID: {empleado['id']}")
        print(f"Nombre: {empleado['nombre']}")
        print(f"Horas trabajadas: {empleado['horas_trabajadas']}")
        print(f"Valor hora: {empleado['valor_hora']}")
    else:
        print('Empleado no encontrado')

def eliminar_empleado(empleados):
    id = input('Ingrese el ID del empleado a eliminar: ')
    empleado = next((e for e in empleados if e['id'] == id), None)
    if empleado:
        empleados.remove(empleado)    
        guardar_archivo(empleados)
    else:
        print('Empleado no encontrado')

def listar_empleados(empleados):
    for empleado in empleados:
        print(f"ID: {empleado['id']}")
        print(f"Nombre: {empleado['nombre']}")
        print(f"Horas trabajadas: {empleado['horas_trabajadas']}")
        print(f"Valor hora: {empleado['valor_hora']}")
        print()

def listar_nomina_empleado(empleados):
    id = input('Ingrese el ID del empleado a listar su nómina: ')
    empleado = next((e for e in empleados if e['id'] == id), None)
    if empleado:
        nomina = empleado['horas_trabajadas'] * empleado['valor_hora']
        print(f"Nómina del empleado {empleado['nombre']} (ID: {empleado['id']}): ${nomina}")
    else:
        print('Empleado no encontrado')

def listar_nomina_todos_empleados(empleados):
    for empleado in empleados:
        nomina = empleado['horas_trabajadas'] * empleado['valor_hora']
        print(f"Nómina del empleado {empleado['nombre']} (ID: {empleado['id']}): ${nomina}")

def menu():
    empleados = leer_archivo()
    while True:
        print('*** NOMINA ACME ***')
        print('MENU')
        print('1- Agregar empleado')
        print('2- Modificar empleado')
        print('3- Buscar empleado')
        print('4- Eliminar empleado')
        print('5- Listar empleados')
        print('6- Listar nómina de un empleado')
        print('7- Listar nómina de todos los empleados')
        print('8- Salir')
        opcion = int(input('Escoja una opción (1-8)? '))
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
            listar_nomina_empleado(empleados)
        elif opcion == 7:
            listar_nomina_todos_empleados(empleados)
        elif opcion == 8:
            break

if __name__ == '__main__':
    menu()
