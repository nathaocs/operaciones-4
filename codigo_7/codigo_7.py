# Estudiante: corrige este código y haz un pull request con la versión corregida.
def validar_email(correo):
    if "@" and "." in correo:
        return True
    return False

print(validar_email("usuario.com"))
