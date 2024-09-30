Clase = { 
'Nombre_clase': 'Spanglish 1', 
'Alumnos':{ 'Nombre': 'Yeison', 'Edad1':14,
        'Nombre': 'Daiyan', 'Edad2':13,
        'Nombre': 'Braiyan', 'Edad3':16   
        },     
}
print("¿La edad de que alumno buscas? Yeison/Daiyan/Braiyan")
name=input()
if name == 'Yeison':
    print (Clase['Alumnos']['Edad1'])
elif name == 'Daiyan':
    print (Clase['Alumnos']['Edad2'])
else:
    print (Clase['Alumnos']['Edad3'])