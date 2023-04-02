"""
# Condicional IF

SI se_cumple_esta_condicion:
    Ejecutar grupo de instrucciones
SI NO:
    Se ejecutan otro grupo de instrucciones

if condicion:
    instrucciones
else:
    otras instrucciones


# Operadores de comparacion

== igual
!= diferente 
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que

# Operadores logicos

and = y
or = o
! = negacion
not = no
"""

# Ejemplo 1
print("################ EJEMPLO 1 ################")
color = "negro"
#color = input("Adivina mi color favorito: ")

if color == "rojo":
    print("El color es ROJO")
else:
    print("El color NO es CORRECTO")


# Ejemplo 2
print("################ EJEMPLO 2 ################")
year = 2019
#year = int(input("Introduce un año: "))

if year >= 2021:
    print("Estamos de 2021 en adelante")
else:
    print("Es un año anterior a 2021")


# Ejemplo 3
print("################ EJEMPLO 3 ################")
nombre = "Miguel Hidalgo"
ciudad = "Panamá"
continente = "America"
edad = 17
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad !!")
    if continente != "America":
        print("El usuario no es Americano")
    else:
        print(f"Es Americano de {ciudad}") 
else:
    print(f"{nombre} NO es mayor de edad")


# Ejemplo 4
print("################ EJEMPLO 4 ################")
dia = 1

if dia == 1:
    print("Es Lunes")
elif dia == 2:
    print("Es Martes")
elif dia == 3:
    print("Es Miercoles")
elif dia == 4:
    print("Es Jueves")
elif dia == 5:
    print("Es Viernes")
else:
    print("Es fin de semana")
