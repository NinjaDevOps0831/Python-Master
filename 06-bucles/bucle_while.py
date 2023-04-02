"""
# WHILE
Estructura de conttrol que itera la ejecucion de una serie de una
Seria de instrucciones tantas veces como sea necesario, hasta que deje de cumplirse la condicion

while condicion:
    bloque de instrucciones
    actualizacion de contador

"""
contador = 1
muestrame = str(0)
while contador <= 100:
    muestrame = muestrame + " , " + str(contador)
    contador+=1
print(muestrame)