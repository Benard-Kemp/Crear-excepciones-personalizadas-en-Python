class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, retiro):
        self.saldo = saldo
        self.retiro = retiro
        super().__init__(f"Saldo insuficiente: saldo={saldo}, retiro={retiro}")

def retirar(saldo, monto):
    if monto > saldo:
        raise SaldoInsuficienteError(saldo, monto)
    return saldo - monto

try:
    retirar(100, 150)
except SaldoInsuficienteError as e:
    print(e)
    print("Saldo:", e.saldo)
    print("Retiro:", e.retiro)
