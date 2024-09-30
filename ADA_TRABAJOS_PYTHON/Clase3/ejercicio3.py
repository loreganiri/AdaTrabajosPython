x = []
cant = int(input("¿Cuantos elementos deseas en esta lista? "))
print(f"La lista contendrá {cant}  numeros")
for i in range(0, cant):
    item = int(input("Dame el numero: "))
    x.append(item)  
print(f"Esta es tu lista llena: {x}")

numrep=int(input("¿Cúal numero repetido buscas?"))
y= x.count(numrep)

print(f"El numero {numrep} se repite {y} veces")