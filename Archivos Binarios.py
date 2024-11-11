# Crear y escribir en un archivo binario
with open('archivo_binario.bin', 'wb') as f:
    f.write(b'Este es un archivo binario.')

# Leer el archivo binario
with open('archivo_binario.bin', 'rb') as f:
    contenido = f.read()
    print(contenido)
