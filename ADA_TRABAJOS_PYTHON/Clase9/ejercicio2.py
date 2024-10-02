archivo2 = open('archivo2.txt', 'w')

with open('archivo2.txt', 'w') as archivo2:
    archivo2.write('Este es el nuevo contenido\n')
    archivo2.write('Todo ha sido sobreescrito\n')
    print("Sobreescritura completada")


