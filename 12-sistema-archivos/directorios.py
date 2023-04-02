import os, shutil

# Crear carptea
if not os.path.isdir("./12-sistema-archivos/mi_carpeta"):
    os.mkdir("./12-sistema-archivos/mi_carpeta")
else:
    print("La carpeta ya existe")

"""
# Copiar
ruta_original = "./12-sistema-archivos/mi_carpeta"
ruta_nueva = "./12-sistema-archivos/mi_carpeta_copiada"

shutil.copytree(ruta_original, ruta_nueva)
"""


# Eliminar
"""
os.rmdir("./12-sistema-archivos/mi_carpeta_copiada")
"""