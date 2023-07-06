# N letras del abecedario
abc = list()
while True:
    letra = input("Digite una letra del abecedario ").lower()
    if letra != '0':
        abc.append(letra)
        continue
    else:
        break   
vocales = ("a","e","i","o","u")
contador = 0
for i in abc:
    for j in vocales:
        if i  == j:
            print(f"La vocal {j} se repite => {abc.count(j)}")
        