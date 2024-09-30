numeros = [10, 11, 10, 14, 23, 21, 2, 1]
numbers = []
limpios = set(numeros)
print(limpios)

for limpio in limpios:
    if limpio>15:
        numbers.append(limpio)
    print (limpio)
else:›
    print(".")

print("La nueva lista es: ",numbers)