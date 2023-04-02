"""
Diccionario: tipo de dato que almacena un conjunto 
de datps. en formato clase > valor.
Es parecido a un array asociativo o un objeto json.

"""

persona = {
    "nombre": "Miguel De Jesus",
    "Apellidos": "Hidalgo Rodriguez",
    "web": "bytec.com"
}

print(type(persona))
print(persona)


# lista con diccionarios
contactos = [
    {
        'nombre': "Miguel",
        'email': "miguel@miguel.com"
    },
    {
        "nombre": "Juan",
        "email": "juan@juan.com"  
    },
    {
        "nombre": "salvador",
        "email": "salvador@salvador.com"  
    }
]

print(contactos[0]["nombre"])

print("\nlista de contactos:")
print("--------------------------------------------------------")

for contacto in contactos:
    print(f"Nombre de contacto: {contacto['nombre']}") #! importante solo se acepta las comillas simples.
    print(f"Email de contacto: {contacto['email']}") #! importante solo se acepta las comillas simples.
    print("--------------------------------------------------------")