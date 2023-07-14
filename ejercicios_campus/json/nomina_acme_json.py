import io
import json

def continuar():
    input('Ingrese cualquier tecla para continuar')

def leer_archivo():
    try:
        empleados = []
        with open('emplacme.json', 'r') as f:
            empleados = json.load(f)
        return empleados
    except FileNotFoundError:
        return False
    

def guardar_archivo(empleados):
    with io.open('emplacme.json', 'w') as f:
        json.dump(empleados, f)

def agregar_empleado(empleados):
    print(empleados)
    id = (input('Ingrese el ID del empleado: '))
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
        print('\nEmpleado Modificado con exito')
        print(f"ID: {empleado['id']}")
        print(f"Nombre: {empleado['nombre']}")
        print(f"Horas trabajadas: {empleado['horas_trabajadas']}")
        print(f"Valor hora: {empleado['valor_hora']}\n")
    else:
        print('Empleado no encontrado')

def buscar_empleado(empleados):
    id = input('Ingrese el ID del empleado a buscar: ')
    empleado = next((e for e in empleados if e['id'] == id), None)
    print('-'*15 ,f'Datos del empleado con id {id}','-'*15 )
    if empleado:
        print(f"ID: {empleado['id']}")
        print(f"Nombre: {empleado['nombre']}")
        print(f"Horas trabajadas: {empleado['horas_trabajadas']}")
        print(f"Valor hora: {empleado['valor_hora']}\n")
        
    else:
        print('Empleado no encontrado')

def eliminar_empleado(empleados):
    id = input('Ingrese el ID del empleado a eliminar: ')
    empleado = next((e for e in empleados if e['id'] == id), None)
    if empleado:
        empleados.remove(empleado)    
        guardar_archivo(empleados)
        print(f"\nEmpleado con id {id} eliminado con exito")
    else:
        print('Empleado no encontrado')

def listar_empleados(empleados):
    print('\n','-'*15,'Lista de todos los empleados','-'*15)
    for empleado in empleados:
        print(f"ID: {empleado['id']}")
        print(f"Nombre: {empleado['nombre']}")
        print(f"Horas trabajadas: {empleado['horas_trabajadas']}")
        print(f"Valor hora: {empleado['valor_hora']}")
        print()

def listar_nomina_empleado(empleados):
    id = input('Ingrese el ID del empleado a listar su nómina: ')
    empleado = next((e for e in empleados if e['id'] == id), None)
    print('\n','-'*15 , f'Nomina empleado con id:{id}','-'*15)
    if empleado:
        nomina = empleado['horas_trabajadas'] * empleado['valor_hora']
        print(f"Nómina del empleado {empleado['nombre']} (ID: {empleado['id']}): ${nomina}")
    else:
        print('Empleado no encontrado')

def listar_nomina_todos_empleados(empleados):
    print('-'*15 , f' Nomina de todos los empleados ','-'*15)
    for empleado in empleados:
        nomina = empleado['horas_trabajadas'] * empleado['valor_hora']
        print(f"Nómina del empleado {empleado['nombre']} (ID: {empleado['id']}): ${nomina}")


def menu():
    if leer_archivo() != False:
        empleados = leer_archivo()
    else:
        empleados = []
    while True:
        try:
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
                continuar()
            elif opcion == 2:
                modificar_empleado(empleados)
                continuar()
            elif opcion == 3:
                buscar_empleado(empleados)
                continuar()
            elif opcion == 4:
                eliminar_empleado(empleados)
                continuar()
            elif opcion == 5:
                listar_empleados(empleados)
                continuar()
            elif opcion == 6:
                listar_nomina_empleado(empleados)
                continuar()
            elif opcion == 7:
                listar_nomina_todos_empleados(empleados)
                continuar()
            elif opcion == 8:
                print('Hasta Luego..')
                break
        except ValueError:
            print('\nIngrese una opcion Valida\n')
            continuar()

if __name__ == '__main__':
    menu()