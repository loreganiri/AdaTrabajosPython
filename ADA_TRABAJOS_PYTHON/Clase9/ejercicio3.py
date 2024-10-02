import os

file = 'archivo3.txt'
if os.path.exists(file): 
    os.remove(file)
    print("Este archivo fue eliminado con exito")
else:
    print("No se encontro tal archivo")