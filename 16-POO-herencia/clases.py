# HERENCIA: Es la posibilidad de compartir atributos y metodos entre clases
# y que diferentes clases hereden de otras.

class persona:
    """
    nombres
    apellidos
    altura
    edad
    """

    # Setter y getter
    def getnombre(self):
        return self.nombre

    def getapellido(self):
        return self.apellido

    def getaltura(self):
        return self.altura

    def getedad(self):
        return self.edad

    def setnombre(self, nombre):
        self.nombre = nombre

    def setapellido(self, apellido):
        self.apellido = apellido

    def setaltura(self, altura):
        self.altura = altura

    def setedad(self, edad):
        self.edad = edad

    # Metodos o funciones de persona
    def hablar(self):
        return "Estoy hablando..."

    def caminar(self):
        return "Estoy caminando..."

    def dormir(self):
        return "Estoy durmiendo..."

class Informatico(persona):
    """
    Lenguajes
    experiencia
    """
    def __init__(self):
        self.lenguajes = "Go, C++, JS, Python"
        self.experiencia = 5

    def getlenguajes(self):
        return self.lenguajes

    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes

    def programar(self):
        return "estoy programando"

    def repararPC(self):
        return "He reparado tu ordenador..."

class tecnicoRedes(Informatico):

    def __init__(self):
        super().__init__()              #! Esta linea llama al constructor de la clase padre informatico, para usar sus atributos.
        self.auditarRedes = "Experto"
        self.experienciaRedes = 15

    def auditar(self):
        return "Estoy auditando una red..."
