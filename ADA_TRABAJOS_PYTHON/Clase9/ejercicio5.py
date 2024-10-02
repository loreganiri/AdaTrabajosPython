import csv

fieldnames = ['Nombre', 'Edad','Ciudad']
with open('csvleer.csv', 'w',newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    writer.writerow({'Nombre':'Ana', 'Edad':'35' , 'Ciudad': 'Ensenada' })
    writer.writerows([
                    {'Nombre':'Jorge', 'Edad':'30' , 'Ciudad': 'Ensenada' },
                    {'Nombre':'Analia', 'Edad':'25' , 'Ciudad': 'Ensenada' }
    ])




