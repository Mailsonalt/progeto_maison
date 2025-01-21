num = input("Digite uma lista de números com espaço: ").split()
num = [int(x) for x in num]

numeros_n_rep = sorted(set(num))
print("Os números nao duplicados e em ordem crescente: ", numeros_n_rep)
