 # Importar modulo
import sqlite3


# Conexion
conexion = sqlite3.connect('./17-bases-datos/pruebas.db')


# Crear cursor 
cursor = conexion.cursor()                                          #! el cursor me permite ejecutar consultas


# Crear tabla                                                       #! execute me permite ejecutar consultas
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(255),
    descripcion TEXT,
    precio int(255)
    );
""") 


# Guardar cambios  
conexion.commit()                                                   #! commit me permite guardar-actualizar cambios


# Insertat datos
#cursor.execute("INSERT INTO productos VALUES (null, 'primer producto', 'descripcion de mi producto', 550)")
#conexion.commit()                                                  #! commit me permite guardar-actualizar cambios


# Borrar datos
#cursor.execute("DELETE FROM productos")   
#conexion.commit()


# Insertat muchos registros
productos = [
    ("Ordenador Portatil", "Buen PC", 700),
    ("telefono movil", "Buen telefono", 100),
    ("Motherboard", "Buena motherboard", 200),
    ("tablet", "Buena tablet", 400),
]
#cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)
#conexion.commit()


# Update
cursor.execute("UPDATE productos SET precio=300 WHERE precio=400")  #! UPDATE para actualizar un campo


# Listar o leer datos
cursor.execute("SELECT * FROM productos WHERE precio >= 300;")
productos = cursor.fetchall()

for producto in productos:
    print(producto)                                                 #! se puede acceder al campo especifico como una lista


# Cerrar conexion
conexion.close()