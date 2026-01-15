class ValidacionError(Exception):
    pass

def validar_numero(texto):
    try:
        n = int(texto)
        if n < 0:
            raise ValidacionError("El número no puede ser negativo")
    except ValueError:
        raise ValidacionError("No es un número válido")
    else:
        return n
    finally:
        pass

try:
    print(validar_numero("-1"))
except ValidacionError as e:
    print("Error:", e)
