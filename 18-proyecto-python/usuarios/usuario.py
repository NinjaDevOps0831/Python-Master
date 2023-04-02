import datetime
import hashlib
import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Usuario:
    
    def __init__(self, nombre, apellidos, email, password):

        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def registrar(self):
        fecha = datetime.datetime.now()

        # Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8')) # Encode me permite convertir a bte mi string
        
        sql = "INSERT INTO usuarios VALUES(null,%s,%s,%s,%s,%s)"
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha) # cifrado.hexdigest me guarda el hexadecimal recibido del update().

        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]    # El return devuelve una lista 

        except:
            result = [0, self]                  # El return devuelve una lista
        
        return result

        

    def identificar(self):
        # Consulta para comprobar que existe el usuario
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"

        # Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8')) # Encode me permite convertir a bte mi string

        usuario = (self.email, cifrado.hexdigest())

        cursor.execute(sql, usuario)
        result = cursor.fetchone()

        return result
