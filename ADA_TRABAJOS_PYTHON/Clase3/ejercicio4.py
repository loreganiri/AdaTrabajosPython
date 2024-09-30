x = []
cant = int(input("¿Cuantos elementos deseas en esta lista? "))
print(f"La lista contendrá {cant}  numeros")
for i in range(0, cant):
    item = int(input("Dame el numero: "))
    x.append(item)  
print(f"Esta es tu lista llena: {x}")

ini = int(input("¿En que posicion quieres empezar la suma?: "))
fin = int(input("¿En que posicion quieres terminar la suma?: "))

sublista = x[ini:fin]
print("Lista eslaiceada XD ")
print(sublista)

cuantos = len(sublista)
print("Esta es la cantidad de elementos en tu sublista: ", cuantos)

suma = 0
i=0
for i in range (i,cuantos):
    suma += sublista[i]

print("La suma total es: ", suma)