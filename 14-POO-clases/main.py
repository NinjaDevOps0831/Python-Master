# programacion orientada a objetos (POO o OOP)

# Definir una clase (molde para crear mas objetos de ese tipo
# (Coche) con caracteristicas similares).

class Coche:

    # Atributos o propiedades (variables)
    # Caracteristicas del coche
    color = "rojo"
    marca = "Honda"
    modelo = "CRV"
    velocidad = 230
    caballaje = 140
    asientos = 5

    # Metodos, son acciones que hace el objeto (coche) (son funciones)
    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def setcolor(self, color):
        self.color = color

    def setmodelo(self, modelo):
        self.modelo = modelo

    def getmodelo(self):
        return self.modelo

    def getcolor(self):
        return self.color

    def getvelocidad(self):
        return self.velocidad

# fin definicion clase

# Crear objetos o instanciar la clase

coche = Coche()
print(f"COCHE 1:")

coche.setcolor("amarillo")
coche.setmodelo("HRV")

print(coche.marca, coche.getmodelo() ,coche.getcolor())
print(f"velocidad actual: {coche.getvelocidad()}")

coche.acelerar()
print(f"velocidad nueva actual: {coche.getvelocidad()}")

coche.frenar()
print(f"velocidad nueva actual: {coche.getvelocidad()}")

print("--------------------------------------------")
# Crear mas objetos
coche2 = Coche()
print(f"COCHE 2:")

coche2.setcolor("verde")
coche2.setmodelo("CIVIC")

print(coche2.marca, coche2.getmodelo() ,coche2.getcolor())

