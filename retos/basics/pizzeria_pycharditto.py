

def input_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("!Error! .Digite un valor valido")


def saldo():
    saldo = input_int("Digite la cantidad con la que va a pagar: ")
    return saldo


def pizza():
    while True:
        try:
            tipo_pizza = int(input(
                "Bienvenido, Digite que pizza quiere:\n1.Pizza Margherita\n2.Pizza Pepperoni\n3.Pizza Vegetariana\n4.Pizza Hawaii\n5.Pizza Diavola\n--> "))
            
            if tipo_pizza >0 and  tipo_pizza <=5:
                return tipo_pizza
            else:
                print("!Error! .Seleccione una opcion valida\n")
                pizza()
        except ValueError:
            print("!Error! .Ingrese un numero de la lista ")
            continue


def ing_extras():
    while True:
        try:
            ing = int(input(
                "Seleccione que ingrediente extra quiere:\n1.pepperonni\n2.Jamon\n3.Salsa Tartara\n4.Pollo\n5.Chorizo\n--> "))
            
            if ing >0 and ing <=5:
                match ing:
                    case 1:
                        print("Pepperonni: 1.55$")
                        return 1.55
                    case 2:
                        return 1.99
                    case 3:
                        return 0.5
                    case 4:
                        return 2.15
                    case 5:
                        return 2.99
                    
            else:
                print("!Error! .Seleccione una opcion valida\n")
                pizza()
        except ValueError:
            print("!Error! .Ingrese un numero de la lista ")
            continue


def pedido():
    print("   *** Pizeeria Pycharditto ***  \n")
    ped = pizza()
    match ped:
        case 1:
            precio = 7
            ing = ing_extras()
            total = precio + ing
            cambio = saldo() - total
            print(f'''
                ---         Su pedido           ---
                El total de su pedido es :{total}$
                Su cambio:               {round(cambio,2)}$
                ''')
        case 2:
            precio = 5
            ing = ing_extras()
            total = precio + ing_extras()
            cambio = saldo() - total
            print(f'''
            ---         Su pedido           ---
            El total de su pedido es :{total}$
            Su cambio:                {round(cambio,2)}$
                
                ''')
        case 3:
            precio = 6
            ing = ing_extras()
            total = precio + ing_extras()
            cambio = saldo() - total
            print(f'''
                ---         Su pedido           ---
                El total de su pedido es :{total}$
                Su cambio:                {cambio}$
                
                ''')
        case 4:
            precio = 8.45
            ing = ing_extras()
            total = precio + ing_extras()
            cambio = saldo() - total
            print(f'''
                ---         Su pedido           ---
                El total de su pedido es :{total}$
                Su cambio:                {cambio}$
                
                ''')
        case 5:
            precio = 7
            ing = ing_extras()
            total = precio + ing_extras()
            cambio = saldo() - total
            print(f'''
                ---         Su pedido           ---
                El total de su pedido es :{total}$
                Su cambio:                {cambio}$
                
                ''')

pedido()