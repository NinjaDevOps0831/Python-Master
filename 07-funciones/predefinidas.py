nombre = "MIguel Hidalgo"

#* Funciones Generales
print(type(nombre))
print("\n")

#* Detectar el tipado
comprobar = isinstance(nombre, str)
if comprobar:
    print("La variables es un String")
else:
    print("No es un String")
print("\n")

#* Limpiar espacios
frase = "     Hola      "
print(frase)
print(frase.strip())
print("\n")

#* Eliminar variables
year = 2021
print(year)
del year
print("\n")

#* Comprobar variables vacia
texto = " ff "
if len(texto) <= 0:
    print("Variable vacia")
else:
    print("La variable tiene contenido", len(texto))
print("\n")

#* Encontrar caracteres
frase = "La vida es bella"
print(frase.find("vida"))
print("\n")

#* Reemplazar palabras en un string
nueva_frase = frase.replace("bella", "hermosa")
print(nueva_frase)
print("\n")

#* Mayusculas y Minusculas
print(nombre)
print(nombre.lower()) #? Minuscula
print(nombre.upper()) #? Mayuscula