# Estudiante: corrige este código y haz un pull request con la versión corregido.
def contar_vocales(texto):
    contador = 0
    for letra in texto:
        if letra == 'a' or 'e' or 'i' or 'o' or 'u':
            contador += 1
    return contador

print(contar_vocales("Programacion"))
