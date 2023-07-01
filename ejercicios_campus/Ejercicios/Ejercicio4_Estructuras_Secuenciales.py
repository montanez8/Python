hora = int(input("Ingrese la hora: "))
minutos = int(input("Ingrese los minutos: "))
minutos_extras = int(input("Ingrse los minutos extra: "))

print(f"la hora ingresada es {hora}:{minutos}")


nueva_hora = (hora + ((minutos + minutos_extras) // 60)) % 24
nuevos_minutos = (minutos + minutos_extras) % 60

nueva = f"{nueva_hora}:{nuevos_minutos}"
print("La nueva hora es:", nueva)
