class EdadInvalidaError(Exception):
    pass

def validar_edad(edad):
    if edad < 0:
        raise EdadInvalidaError("La edad no puede ser negativa")
    return edad

try:
    validar_edad(-5)
except EdadInvalidaError as e:
    print("Error:", e)
