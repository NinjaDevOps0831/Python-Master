# capturar excepciones y manejar errores en código
# suscrptible a fallos/errores

"""
try:
    nombre = input("¿Cual es tu nombre?: ")

    if len(nombre) > 1:
        nombre_user = f"el nombre es {nombre}"

    print(nombre_user)

except:
    print("Ha ocurrido un error, coloca un nombre...")
else:
    print("Todo ha funcionado correctamente...")
finally: 
    print("fin de la iteracion try...")

"""


# Manejar multiples excepciones

"""try:
    numero = int(input("Numero para elevarlo al cuadrado: "))
    print(f"el cuadrado es: {str(numero*numero)}")

except TypeError:
    print("Debes convertir tus cadenas a enteros...")
#except ValueError:
    #print("Introduce un numero o valor correcto...")
except Exception as e:

    print(f"Ha ocurrido un error: {type(e).__name__}")

    """

# Excepciones personalizadas o Lanzar excepcion

try:
    nombre = input("¿Cual es tu nombre?: ")
    edad = int(input("Introduce tu edad: "))

    if edad < 5 or edad > 110:
        raise ValueError(" La edad introducida no es real")

    elif len(nombre) <= 1:
        raise ValueError("El Nombre no esta completo")

    else:
        print(f"Bienvenido {nombre}")

except ValueError:
    print("Introduce los datos correctamente...")

