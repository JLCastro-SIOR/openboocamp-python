paises = input("Ingresa una lista de países separados por comas: ")

# Convertir la entrada del usuario en una lista y eliminar espacios en blanco
paises_list = [paises.strip() for paises in paises.split(",")]

# Eliminar duplicados y ordenar alfabéticamente
paises_unicos = sorted(list(set(paises_list)))

# Mostrar la lista ordenada
print(", ".join(paises_unicos))