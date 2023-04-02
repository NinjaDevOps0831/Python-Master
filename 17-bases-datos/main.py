import mysql.connector


# Conexion
database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="master_python"
)

# ¿La conexion ha sido correcta?
#print(database)                     #! <mysql.connector.connection.MySQLConnection object at 0x00000*********>


# Crear cursos para generar consultas o Queries
cursor = database.cursor()

# Crear base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

"""
# Ver base de datos
cursor.execute("SHOW DATABASES")
for db in cursor:
    print(db)

"""

#Crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")
"""
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)

"""


# Insertat datos
#cursor.execute("INSERT INTO vehiculos VALUES(null, 'Opel', 'Astra', 18500)")
#database.commit()

# Insertar datos masivos
"""
coches = [
    ('seat', 'Ibiza', '5000'),
    ('Toyota', 'Hilux', '29000'),
    ('Honda', 'CRV', '30000'),
    ('Nissan', 'L200', '27000'),
]
cursor.executemany("INSERT INTO vehiculos VALUES(null,%s, %s, %s)", coches)
database.commit()

"""

# Sacar informacion de la base de datos
cursor.execute("SELECT * FROM vehiculos")
resultado = cursor.fetchall()

print("---- Todos los coches ----")
for coche in resultado:
    print(coche)

# Borrar datos
cursor.execute("DELETE FROM vehiculos WHERE marca = 'Opel'")
database.commit()
print(cursor.rowcount, "borrados!!")

# Actualizar datos
cursor.execute("UPDATE vehiculos SET modelo='L200 X' WHERE marca='Nissan'")
database.commit()
print(cursor.rowcount, "Actualizado!!")


database.close()
