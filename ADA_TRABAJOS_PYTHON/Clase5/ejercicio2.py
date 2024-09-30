Libro={
'Titulo': 'Extraordinary stories',
'Autor': 'Edgar Allan Poe',
'Año de publicación': '1841',
'Género':'Ficción'
}
Title = Libro['Titulo']
Author = Libro['Autor']
Year = Libro['Año de publicación']
Genre = Libro['Género']

print(Title, Author, Year, Genre)

Libro.update ({'Año de publicación':'1968'})
NewYear = Libro['Año de publicación']
Valores = Libro.values()
print (Valores)

del Libro['Género']
Valores = Libro.values()
print (Valores)
