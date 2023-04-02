# Definir una clase (molde para crear mas objetos de ese tipo
# (Coche) con caracteristicas similares).

from operator import mod
from statistics import mode


class Coche:

    # Atributos o propiedades (variables)
    # Caracteristicas del coche
    color = "rojo"
    marca = "Honda"
    modelo = "CRV"
    velocidad = 230
    caballaje = 140
    asientos = 5

    soy_publico = "Hola soy un atributo publico"
    __soy_privado = "Hola soy un atributo privado"

    def __init__(self, color, marca, modelo, velocidad, caballaje, asientos): #! Así se define un constructor!
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.asientos = asientos
    
    # Metodos, son acciones que hace el objeto (coche) (son funciones)
    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def setcolor(self, color):
        self.color = color

    def setmodelo(self, modelo):
        self.modelo = modelo

    def setmarca(self, marca):
        self.marca = marca

    def getmarca(self):
        return self.marca

    def getmodelo(self):
        return self.modelo

    def getcolor(self):
        return self.color

    def getvelocidad(self):
        return self.velocidad

    def getprivado(self):
        return self.__soy_privado

    def getInfo(self):
        info = "--- Informacion del coche ---"
        info += f"\n Color: { self.getcolor()}"
        info += f"\n Marca: {self.getmarca()}"
        info += f"\n Modelo: {self.getmodelo()}"
        info += f"\n Velocidad: {self.getvelocidad()}"
        return info



# fin definicion clase