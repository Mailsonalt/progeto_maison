class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Inicializando uma conta")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        pass

conta = Conta('123-9', 'Malson', 300, 400)
print(conta)

