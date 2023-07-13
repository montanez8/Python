import json

dic = {1: "lapiz" , 2:"Borrador" , 3:"Cuaderno" ,4: "Lapicero" , "Valor":2500}
dic2 = {
    "infliencers":[
        {
        "name":"Jaxon",
        "age":42,
        "word at":"Tech news"
        },
        {
        "name":"Miller",
        "age":35,
        "word at":"IT Day"
        }
    ]
    
}
with open("Python/clases/Ejercicios_clase_10_07_archivos/diccioanrio.json", "w")as archivo:
    json.dump(dic, archivo)
    json.dump(dic2 , archivo)

if not archivo.closed:
    print("Cerrando archivo")
    archivo.close()
    
    
    