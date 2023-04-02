"""
Modulos: son funcionalidades ya hechas para reutilizar.
en python hay muchos por defectos en: #* https://docs.python.org/3/py-modindex.html

Podemos conseguir modulos que ya vienen en el lenguaje, modulos en internet y tambien 
podemos crear nuestros modulos.

"""

# importar mi propio modulo
import modulo

print(modulo.holamundo("Miguel"))
print("-----------------------------------------------")


# Modulo fechas
import datetime
print(datetime.date.today())

fecha_completa = datetime.datetime.now()
print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.time())

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M") #! formateando fecha
print(f"Fecha Personalizada: {fecha_personalizada}")
print("-----------------------------------------------")


# Modulo de matematica
import math

print("Raiz Cuadrada de 10: ", math.sqrt(10))
print("NUmero PI: ", math.pi)
print("Redondear: ", math.ceil(6.56789))
print("-----------------------------------------------")


# Modulo Randon
import random

print(f"Numro Aleatorio 15 - 67: {random.randint(15, 67)}")



