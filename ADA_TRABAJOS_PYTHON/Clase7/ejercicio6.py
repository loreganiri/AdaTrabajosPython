
numeros = []
cubos = []
for i in range(1,16):
    print("Numero", i)    
    if i % 2 == 0:
        cubos = [x**3 for x in range(1,16)]

print("cubo", cubos)

