dic_categoria = {1:25000 , 2:30000 , 3:40000 , 4:45000 , 5:60000}
tot_honorarios = 0
docentes = {}
while True:
    try:
        cedula = int(input("Ingrese cedula docente: "))
        nombre = input("Ingrese nombre del docente: ")    
        cat = int(input("Ingrese categoria del docente: "))
        horas = int(input("Horas laboradas en el mes por el docente: "))
        docentes[cedula]={}
        docentes[cedula]["nombre"]= nombre
        docentes[cedula]["categoria"]=cat
        docentes[cedula]["horas"]=horas
        
        opc = input("Desea agregar otro docente (S/N)?")
        if opc.lower() == "n":
            break
    except ValueError:
        print("!Eror! ")
print("\n\n *** Informe ***")
print("=" * 30)
for k in docentes.keys():
    h = docentes[k]["horas"] * dic_categoria[docentes[k]["categoria"]]
    tot_honorarios +=h
    print(docentes[k]["nombre"] , f" -- ${h:,}")
    print("-"*30)
    print(f"Total honorarios docentes : ${tot_honorarios:,}\n") 
    
    
    