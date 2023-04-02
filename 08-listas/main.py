peliculas = ["batman", "SpiderMan", "Coco"]
cantantes = list(("2pac", "Drake", "Jennifer Lopez"))

# Indices:
print(peliculas)
print(peliculas[1])
print(peliculas[1:3])
print(peliculas[2:])

# Añadir elementos a las listas:
cantantes.append("BadBunny")
print(cantantes)

# recorrer lista:
print("************** LISTADO PELICULAS****************")
for pelicula in peliculas:
    print(pelicula)
