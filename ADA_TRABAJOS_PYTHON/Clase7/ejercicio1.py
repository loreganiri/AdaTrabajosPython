cuadrado = []
lixta = []

for i in range(10):
    lixta = list(range(10))

for i in lixta:
    if lixta[i] % 2 == 0:
        x=lixta[i]**2
        cuadrado.append(x)
        
print(f"Esta es la lista original creada con range: ",lixta)
print(f"Esta es la lista de los cuadrados: ",cuadrado)
    




