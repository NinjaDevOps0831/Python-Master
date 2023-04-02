"""
FUNCIONES:
Una funcion es un conjunto de instrucciones agrupadas bajo un nombre concreto
que pueden reutilizarse invocando a la funcion tantas veces como sea necesario.

def nombre_de_funcion(parametros):
    # BLOQUE / INSTRUCCIONES

nombre_defuncion(mi_parametro)



# Ejemplo1
def muestraNombres():
    print("Miguel")
    print("Delvis")
    print("Oscar")
    print("Martin")
    print("Maruchan")
    print("\n")

muestraNombres()


# Ejemplo 2 - Parametros Opcionales
print("###### Parametros Opcionales ######")

def getempleado(nombre, dni = None):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")
    if dni != None:
        print(f"DNI: {dni}")

getempleado("Miguel Hidalgo")


# Ejemplo 3 - Parametros Opcionales y return
print("######  Return ######")
def saludame(nombre):
    saludo = f"Hola, Saludos {nombre}"

    return saludo

print(saludame("Miguel Hidalgo"))
"""

# Ejemplo 4 - Funciones lambda
print("######  Funciones Lambda ######")
dime_year = lambda year: f"El año es {year}"
print(dime_year(2021))
