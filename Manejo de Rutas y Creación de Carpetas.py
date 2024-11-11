import os
from pathlib import Path

# Crear una carpeta usando os
os.makedirs("nueva_carpeta/os", exist_ok=True)

# Crear una carpeta usando pathlib
Path("nueva_carpeta/pathlib").mkdir(parents=True, exist_ok=True)

# Ver ruta absoluta del archivo actual
print(Path(__file__).absolute())
