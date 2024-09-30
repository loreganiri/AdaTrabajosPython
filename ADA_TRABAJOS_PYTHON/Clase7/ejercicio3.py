conjunto_1 = {1, 2, 3, 4}
conjunto_2 = {3, 4, 5, 6}
print ("Este es el conjunto 1: {conjunto_1}")
print("Este es el conjunto 2: {conjunto_2}")

conjunto_1.update(conjunto_2)
print("La union del conjunto uno con el dos", conjunto_1)
conjunto_1 = {1, 2, 3, 4}
conjunto_2 = {3, 4, 5, 6}
conjunto_1.intersection_update(conjunto_2)
print("La interseccion del conjunto uno con el dos :", conjunto_1) 
conjunto_1 = {1, 2, 3, 4}
conjunto_2 = {3, 4, 5, 6}
conjunto_1.difference_update(conjunto_2)
print("La diferencia del conjunto uno menos el dos ",conjunto_1)

#Nota, tuve que repetir los conjuntos por que por alguna razon mi maquina
#borraba los datos y no arrojaba el resultado correcto, hice miles de prints paso por
#paso y cuando los unia me vaciaba los sets, por eso termine haciendo esto, sorry!

