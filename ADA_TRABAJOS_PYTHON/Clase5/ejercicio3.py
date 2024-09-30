Persona = {
    'Name' : 'Lorraine', 
    'Edad' : 41,
    'Dirección' : {'Calle': 'Niza', 
               'Ciudad' : 'Ensenada',
               'Codigo postal': '22880'
         }
}
print(Persona)
city = Persona['Dirección']['Ciudad']
print("Ciudad: ", city)


