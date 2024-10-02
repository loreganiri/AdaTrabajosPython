import csv
with open('csvleer.csv', 'r') as hoja:
    reader = csv.reader(hoja)

    for fila in reader:
        print(fila)
