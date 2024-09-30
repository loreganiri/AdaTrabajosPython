lista_animales = ["perro", " ", "gato", "raton", "pajaro", " ", "pez"]
short_list = []
for i in range(len(lista_animales)):
    print(lista_animales[i])

print ("Ahora sin espacios vacios")

for indice, nombre in enumerate(lista_animales):
    if len(nombre)<=5: 
        if nombre == " ":
            continue
        short_list.append(nombre)
        for x in enumerate(short_list):
            print(x)
    else:
        break

