from coche import Coche

carro = Coche("amarillo", "toyota", "Hilux", 200, 290, 5)
carro1 = Coche("blanco", "toyota", "Hilux", 200, 280, 5)
carro2 = Coche("verde", "toyota", "Hilux", 200, 240, 5)
carro3 = Coche("negro", "toyota", "Hilux", 200, 275, 5)

print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())

# Detectar tipado
if type(carro3) == Coche:
    print("Es un objeto correcto...")
else:
    print("No es un objeto")

# visibilidad (atributos publcios o privados)
print(f"-----------------------")
print(carro.soy_publico)
print(carro.getprivado())