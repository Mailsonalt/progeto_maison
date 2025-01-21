matriz = []
print("Digite os valores para a matriz 2x3: ")
for i in range(2):
    linha = []
    for j in range(3):
        valor = float(input(f"Digite o valor para a posição 1: "))
        valor = float(input(f"Digite o valor para a posição 2: "))
        valor = float(input(f"Digite o valor para a posição 3: "))
        linha.append(valor)
        matriz.append(linha)
        

        soma = 0 
        for linha in matriz:
            soma += sum(linha)

            print("\nMatriz: ")
            for linha in matriz:
                print(linha)
            print(f"\nSoma de todos os elementos: {soma}")
            