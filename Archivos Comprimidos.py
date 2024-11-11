import zipfile

# Crear y escribir en un archivo comprimido
with zipfile.ZipFile('archivo.zip', 'w') as z:
    z.write('archivo_texto.txt')
    z.write('archivo_binario.bin')

# Leer el contenido de un archivo comprimido
with zipfile.ZipFile('archivo.zip', 'r') as z:
    z.extractall('descomprimido')
    print(z.namelist())
