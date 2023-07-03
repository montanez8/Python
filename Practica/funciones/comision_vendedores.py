def input_string(msg):
    while True:
        try:
            return input(msg)
        except:
            print('!Error! Digite una Cadena de caracteres')


def datos_vendedor():
    vendedores = []
    while True:
        cedula_ciu = input_string('Digite el numero de cedula del vendedor: ')
        nombre = input_string('Digite el nombre del vendedor: ')
        valor_ventas = int(input('Ingrese el valor total de ventas: '))
        vendedor = [cedula_ciu, nombre , valor_ventas]
        vendedores.append(vendedor)
        op = input_string(
            'Desea ingresar otro vendedor\n.SI\n.NO\n-->').upper()
        if op == 'SI':
            continue
        else:
            break
    return vendedores


def tipo_vendedor():
    while True:
        try:
            tipo = int(input(
                'Digite el tipo de vendedor\n1.Puerta a puerta\n2.Telemercadeo\n3.Ejecutivo de ventas\n--> '))
            if tipo > 0 and tipo < 4:
                if tipo == 1:
                    nom_tipo = 'Puerta a Puerta'
                    comision = 0.2
                    datos_tipo = [nom_tipo, comision]
                    return datos_tipo
                elif tipo == 2:
                    nom_tipo = 'Telemercadeo'
                    comision = 0.15
                    datos_tipo = [nom_tipo, comision]
                    return datos_tipo
                else:
                    nom_tipo = 'Ejecutivo de ventas'
                    comision = 0.25
                    datos_tipo = [nom_tipo, comision]
                    return datos_tipo
            else:
                print('Digite una opcion correcta\n')

        except:
            print('!Error! Ingrese un numero valido (1 a 3)\n')


vendedores = datos_vendedor()
j = 0
for i in vendedores:
    print(f'Seleccione que tipo de vendedor es: {vendedores[j][1]}')
    tipo = tipo_vendedor()
    valor_ventas = vendedores[j][2]
    nombre = vendedores[j][1]
    j +=1
    comision = tipo[1]
    total = (valor_ventas * comision)
    print(f'El vendedor {nombre} tiene un total de ventas de ${valor_ventas:,} y le corresponde una comision de ${total:,} ')
    
    
        

        
