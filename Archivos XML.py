import xml.etree.ElementTree as ET

# Crear y escribir en un archivo XML
root = ET.Element("biblioteca")
libro = ET.SubElement(root, "libro")
titulo = ET.SubElement(libro, "titulo")
titulo.text = "Python para principiantes"
autor = ET.SubElement(libro, "autor")
autor.text = "Juan Pérez"

tree = ET.ElementTree(root)
tree.write("archivo.xml")

# Leer el archivo XML
tree = ET.parse("archivo.xml")
root = tree.getroot()

for libro in root:
    for elemento in libro:
        print(f"{elemento.tag}: {elemento.text}")
