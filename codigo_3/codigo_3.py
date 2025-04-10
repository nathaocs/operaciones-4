# Estudiante: corrige este código y haz un pull request con la versión corregida.
def dividir_listas(lista1, lista2):
    resultado = []
    for i in range(len(lista1)):
        resultado.append(lista1[i] / lista2[i])
    return resultado

print(dividir_listas([4, 8], [2, 0]))
