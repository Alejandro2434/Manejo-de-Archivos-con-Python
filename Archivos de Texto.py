# Crear y escribir en un archivo de texto
with open('archivo_texto.txt', 'w') as f:
    f.write('Hola, este es un archivo de texto en Python.\n')
    
# Leer el archivo de texto
with open('archivo_texto.txt', 'r') as f:
    contenido = f.read()
    print(contenido)
    
# Agregar texto al archivo
with open('archivo_texto.txt', 'a') as f:
    f.write('Agregando una nueva línea al archivo de texto.\n')
