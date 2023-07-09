hora = int(input('digite la hora: '))
minutos = int(input('minutos : '))
segundos = int(input('segundos: '))
formato = input('digite el formato AM , PM: ')
formato =formato.upper()
print(formato)
if(formato == "PM"):
    hora = hora + 12
    if hora == 24:
        hora = 00
else:
    hora = hora
    
print(f'la nueva hora es {hora}:{minutos}:{segundos}')