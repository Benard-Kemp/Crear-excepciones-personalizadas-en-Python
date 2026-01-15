class AppError(Exception):
    pass

class ValidacionError(AppError):
    pass

def validar(nombre):
    if not nombre:
        raise ValidacionError("El nombre no puede estar vacío")

try:
    validar("")
except AppError as e:
    print("Error de la aplicación:", e)

