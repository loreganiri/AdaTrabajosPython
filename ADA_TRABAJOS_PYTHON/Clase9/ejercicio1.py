archivo = open('mi_archivo.txt', 'r')

with open('mi_archivo.txt', 'r') as archivo:
    print("Leyendo el archivo con read")
    contenido = archivo.read()
    print(contenido)
    print("-"*40)

