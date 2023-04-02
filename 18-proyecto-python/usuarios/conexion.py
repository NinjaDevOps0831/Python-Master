from sqlite3 import Cursor
import mysql.connector


def conectar():
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="master_python",
        port=3306
    )
    
    cursor = database.cursor(buffered=True)

    return [database, cursor]   # El return devuelve una lista.
