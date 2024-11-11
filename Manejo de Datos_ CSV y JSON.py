import csv

# Crear y escribir en un archivo CSV
with open('archivo.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Nombre', 'Edad'])
    writer.writerow(['Ana', 23])
    writer.writerow(['Luis', 30])

# Leer el archivo CSV
with open('archivo.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
