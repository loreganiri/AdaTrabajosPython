lista = []
lista_3 = set()

for i in range(20):
    lista = list(range(20))
    if i % 3 == 0:
        continue       
    if i > 15:
        break
    lista_3.add(i)       
x = any(i %2==0 for y in lista_3)

print(f"Lista original: {lista}")
print(f"Lista divisible entre 3 {lista_3}")
print(f"Hay pares?{x}")
