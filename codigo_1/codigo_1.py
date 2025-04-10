# Estudiante: corrige este código y haz un pull request con la versión corregida.
def buscar_elemento(lista, objetivo):
    for i in lista:
        if i == objetivo:
            print("Elemento encontrado en la posición", i)
            return True
        else:
            return False

lista = [3, 7, 9, 2]
print(buscar_elemento(lista, 9))
