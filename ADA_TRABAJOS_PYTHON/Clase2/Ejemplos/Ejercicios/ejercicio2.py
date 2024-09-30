age = int(input ("Introduce tu edad: "))

print("Tu respuesta fue: ",age)
b = int(60)
if age <=12 :
  print("Eres un bebesito")
else:
    if age <=19 :
       print("Eres un adolescente")
    else:
       if age <= 64:
          print("Es un adulto")
       else:
          print("Es usted un adulto mayor")