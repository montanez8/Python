import io

# abrirlo
fd = open("clases/Codigo_clases/archivos/mbox-short.txt", "r", encoding="utf-8")
fd.seek(55)
# leer = fd.read()
leer2 = fd.readline(6)
leer3 = fd.readlines()
fd.close()

print(leer2.rstrip())
print(leer3)

