import random

aleatorios = []
excluidos = []


for i in range(10):
    x = random.randint(0,20)
    if x>10:
        continue    
    if x%15==0:
        break   
    aleatorios.append(x)
    print(aleatorios)   

excluidos=[x for x in aleatorios if x>10 and x%15!=0]
excluidos.append(x)
print("Excluido",x)
    




