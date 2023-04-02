"""
Proyecto Python y MySQL:

- Abrir asistente
- Login o registro
- Si elegimos registro, creará un usuario en la base de datos
- Si elegimos login, identifica al usuario y nos preguntará
- Crear nota, mostrar nota, borrar nota.

"""

from usuarios import acciones


print("""
Acciones disponibles:
    - Registro
    - Logins
""")

hazEl = acciones.Acciones()
accion = input(f"¿Qué quieres hacer?: ")

if accion == "registro":
    # Agregar accion registro de la clase Acciones()
    hazEl.registro()

elif accion == "login":
    # Agregar la accion login de la clase Acciones()
    hazEl.login()