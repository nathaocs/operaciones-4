# Estudiante: corrige este código y haz un pull request con la versión corregida.
def es_primo(n):
    if n == 1:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
        else:
            return True

print(es_primo(9))
