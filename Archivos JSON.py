import json

# Crear y escribir en un archivo JSON
data = {'Nombre': 'Ana', 'Edad': 23}
with open('archivo.json', 'w') as jsonfile:
    json.dump(data, jsonfile)

# Leer el archivo JSON
with open('archivo.json', 'r') as jsonfile:
    data = json.load(jsonfile)
    print(data)
