nm = int(input("Digite um numero inteiro positivo: "))

if nm <= 0:
    print("Número invalido. Digite um número positivo")
else:
    soma_divisores = 0
    for i in range(1, nm):
        if nm % i == 0:
            soma_divisores += i
            if soma_divisores == nm:
                print(f"{nm} é um número perfeito.")
            else:
                print(f"{nm} não é um número perfeito")
