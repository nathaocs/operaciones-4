def contar_vocales(texto):
    contador = 0
    for letra in texto.lower():
        if letra in 'aeiou':
            contador += 1
    return contador

print(contar_vocales("Programacion"))
