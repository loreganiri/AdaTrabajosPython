edad = 25
nombre = "Anna"
esta_estudiando = True

Pi = 3.14
Pais = "Argentina"

edad = int(input ("Introduce tu edad: "))
nombre = input("Introduce tu nombre: ")
esta_estudiando = input("¿Estás estudiando?(si/no):").lower() == "sí"

cantidad_de_libros = 10
titulo_libro = "El principito"
es_interesante = True
temas = ["Aventura", "Fantasia", "Filosofia"]
autor = {"nombre" : "Antoine de Saint-Exupery", "Nacionalidad": "Francesa"}

edad_str = str(edad)
cantidad_de_libros_float = float(cantidad_de_libros)

print("Nombre: ", nombre)
print("Edad: ", edad)
print("¿Esta estuandiando?") 
print("Constante Pi: ", Pi)
print("Constante PAIS:", Pais)
print("Cantidad de libros: ", cantidad_de_libros)
print("Titulo del libro: ", titulo_libro)
print("¿Es interesante?: ", es_interesante)
print("Temas del libro: ", temas)
print("Autor del libro: ", autor)
print("Edad como cadena de texto: ", edad_str)
print("Cantidad de libros como float: ", cantidad_de_libros_float)