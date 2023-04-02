import clases

persona = clases.persona()
persona.setnombre("Miguel")
persona.setapellido("Rodriguez")
persona.setaltura("175cm")
persona.setedad("22 años")

print(f"La persona es: {persona.getnombre()} {persona.getapellido()}")
print(persona.hablar())

print(f"-------------------------------------")

informatico = clases.Informatico()
informatico.setnombre("Carlos")
informatico.setapellido("Martinez")
print(f"El informatico es: {informatico.getnombre()} {informatico.getapellido()} ")
print(informatico.getlenguajes())
print(informatico.experiencia)

print(f"-------------------------------------")

tecnico = clases.tecnicoRedes()
tecnico.setnombre("Manolo")
print(tecnico.auditarRedes, tecnico.getnombre(), tecnico.getlenguajes())

print(f"-------------------------------------")

