Nombres = []

print("Que nombre(s) deseas agregar?, Escribe 'Carlos' cuando ya no quieras agregar mas")
while True:
    nombre = input()
    Nombres.append(nombre)
    if nombre == "Carlos":
        break
for indice, name in enumerate(Nombres):
    if Nombres[indice].startswith("A"):
        continue
    
    print(f"Indice{indice}:{name}")

