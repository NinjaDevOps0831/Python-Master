cantantes = ["2pac", "Drake", "Jennifer Lopez"]
numeros = ["1", "0", "2"]

# Ordenar:
print(numeros)
numeros.sort()
print(numeros)

# Añadir elementos:
cantantes.append("BadBunny")
print(cantantes)

cantantes.insert(1,"Boza")
print(cantantes)

# eliminar elementos:
cantantes.pop(1)
print(cantantes)

cantantes.remove("Drake")
print(cantantes)

# Dar la vuelta:
numeros.reverse()
print(numeros)

# Buscar dentro de una lista:
print("2pac" in cantantes)

# contar elementos:
print(len(cantantes))

# cuantas veces se repite un elemento:
print(numeros.count("2"))

# obtener indice:
print(cantantes.index("2pac"))

# Unir listas:
cantantes.extend(numeros)
print(cantantes)