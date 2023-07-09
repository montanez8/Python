# diccionario vacio
my_dict = {}
my_dict = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "New York" 
}

my_dict["nombre"]  # Juan
my_dict.get("edad") # 30

# anadir nuevos elementos 
my_dict["pais"] = "EEUU"

# actualizar valores 
my_dict["edad"] = 38
my_dict["pais"] = "Colombia"
my_dict["ciudad"] = "Bucaramanga"


# recorrer un diccionario 
for key in my_dict:
    print(key.capitalize(), " : ", my_dict[key])

# tamano del diccionario
len(my_dict)


# verifficar si existe una clave

"nombre" in my_dict   # True
"direccion" in my_dict # False


# variar diccionario  my_dict = {} elimina todos los elementos del diccinario

