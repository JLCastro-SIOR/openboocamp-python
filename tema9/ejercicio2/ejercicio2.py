from functools import reduce

def obtener_impares_y_sumarlos(numeros):
    # Obtener los números impares de la lista usando filter
    impares = filter(lambda x: x % 2 != 0, numeros)
    # Sumar los números impares usando reduce
    suma = reduce(lambda x, y: x + y, impares)
    return suma

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = obtener_impares_y_sumarlos(numeros)
print(resultado)