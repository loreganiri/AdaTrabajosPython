class Estudiante:
    def _init_(self, nombre, edad, ingles, matematicas, biologia):
        self.nombre = nombre
        self.edad = edad
        self.ingles = ingles
        self.matematicas = matematicas
        self.biologia = biologia

def calc_prom(ingles, matematicas, biologia):
    prom=(ingles+matematicas+ingles)/3
    return prom
    
count1 = 0
count2 = 0 

print("Nombre:")
nombre = str(input())
print("Edad:")
edad = int(input())
print("Ingles:")
ingles = float(input())
print("Matematicas:")
matematicas = float(input())
print("Biologia:")
biologia = float(input())
prom = calc_prom(ingles, matematicas, biologia)

if prom > 6:
    print("Aprobado con ", prom)
    count1 +=1
else:
    print("Reprobado con: ", prom)
    count2 +=1






