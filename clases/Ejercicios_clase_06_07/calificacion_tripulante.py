notas = {"nota_1": 0.3,"nota_2": 0.3,"nota_3": 0.4}
estudiantes = {}

def calcular_notas(estudiantes , notas):
    prom_not1 = 0
    prom_not2 = 0    
    prom_not3 = 0
    
    for k in estudiantes.keys():
        prom_not1 = estudiantes[k]["nota1"] * notas["nota_1"]
        prom_not2 = estudiantes[k]["nota2"] * notas["nota_2"]
        prom_not3 = estudiantes[k]["nota3"] * notas["nota_3"]
        nota_definitiva = prom_not1 + prom_not2 + prom_not3
        if nota_definitiva >= 3.0:
            print(f"El estudiante Aprobo con una nota de {nota_definitiva}")
        else:
            print(f"El estudiante Reprobo con una nota {nota_definitiva} ")
        
while True:
    try:
        cod = int(input("Ingrese el codigo del estudiante: "))
        salir = 999
        if cod == salir:
            break
        nombre = input("Ingrese el nombre del estudiante: ")
        nota_1 = float(input("Ingrese la nota 1 del estudiante: "))
        nota_2 = float(input("Ingrese la nota 2 del estudiante: "))
        nota_3 = float(input("Ingrese la nota 3 del estudiante: "))
        estudiantes[cod]= {}
        estudiantes[cod]["nombre"]= nombre
        estudiantes[cod]["nota1"]=nota_1
        estudiantes[cod]["nota2"]=nota_2
        estudiantes[cod]["nota3"]=nota_3
    except ValueError:
        print("!Error!")
print(estudiantes)      
calcular_notas(estudiantes ,notas)