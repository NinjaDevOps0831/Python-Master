"""
* Variable Local: Se define dentro de la funcion, si quieres hacerla #!Global
*                 Entonces usa la funcion "global"

? Variable Globales: Se declaran fuera de las funciones
?                    estan disponibles fuera y dentro de ellas.
"""

# *Variable Global
frase = "Ni los genios son tan genios, ni los mediocres tan mediocres"

def holaMundo():
    frase = "Hola Mundo"  #* Variable Local
    print(frase)
