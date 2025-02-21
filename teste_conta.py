from conta import Conta
#conta = {"numero": '123-4', "titular": "João", "saldo": 120.0, "limite": 1000.0}
#conta1 = {"numero": '123-5', "titular": "Maria", "saldo": 500.0, "limite": 2000.0}
#conta2 = {"numero": '123-6', "titular": "Pedro", "saldo": 50.0, "limite": 12000.0}

def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}

    return conta

#conta1 = cria_conta('123-4', 'joão', 100, 500)
#conta2 = cria_conta('123-5', 'Maria', 500, 1500)

#print(conta1)
#print(conta2)

def deposita(conta, valor):
    conta['saldo'] += valor


def saca(valor):
    conta['saldo'] -= valor


def extrato(conta):
    print("numero: {} \nsaldo: {}".format(conta['numero'], conta['saldo']))

#conta = cria_conta('123-9', 'Malson', 300, 400)
#print(conta)
#deposita(conta, 100)
#print(conta)
#saca(conta, 200)
#print(conta)
#extrato(conta)

conta = Conta('123-9', 'Mailson', 300, 4000000)
print(conta.titular)
print(conta.saldo)
print(conta.limite)
