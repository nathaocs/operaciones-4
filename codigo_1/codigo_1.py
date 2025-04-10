# Estudiante: corrige este código y haz un pull request con la versión corregida.
lista = [3, 7, 9, 2]

def buscar_elemento(lista, objetivo):
    for i in range(len(lista)): 
        if lista[i] == objetivo:
            print("Elemento encontrado en la posición", i)
            return True
    return False 

print(buscar_elemento(lista, 9))
