#x = int(input("Digite o primeiro numero: "))
#y = int(input("Digite o primeiro segundo: "))
#z = int(input("Digite o primeiro terceiro: "))
#print(max(x, y, z))


#Ex2
#num1 = int(input("Digite um número: "))
#num2 = int(input("Digite um número: "))
#num3 = int(input("Digite um número: "))

#if num1 and num2 == num3:
#    print("Esta forma geométrica é equilátera")
#elif num1 or num2 == num3:
#    print("Forma geométrica Isóceles")
#else:
#    print("forma geométrica escaleno")





#Ex3
#n = int(input("Digite um número inteiro positivo: "))
#soma_pares = 0 

#for i in range(1, n + 1):
#    if i % 2 == 0:
#        soma_pares += i

#print(f"A soma de todos os números pares de 1 até {n} é: {soma_pares}")


#Ex4
#nm = int(input("Digite um numero inteiro positivo: "))

#if nm <= 0:
#    print("Número invalido. Digite um número positivo")
#else:
#    soma_divisores = 0
#    for i in range(1, nm):
#        if nm % i == 0:
#            soma_divisores += i
#            if soma_divisores == nm:
#                print(f"{nm} é um número perfeito.")
#            else:
#                print(f"{nm} não é um número perfeito")


#ex5
#def eh_palindromo(palavra):
#    palavra = palavra.lower().replace(" ", "")
#    return palavra == palavra[::-1]
#palavra = input("Digite uma frase: ")
#print(palavra[::-1])

#if eh_palindromo(palavra):
#    print("A palavra é um palindromo")
#else:
#    print("A palavra não é um palindromo")
#eh_palindromo

#Ex 7
#nm = int(input("Digite um número inteiro positivo: "))
#if nm <= 1:
#    print("Não é primo")
#elif nm == 2:
#    print("É primo")
#elif nm % 2 == 0:
#    print("Não é primo")
#else:
#    primo = True
#    for i in range(3, int(nm ** 0.5) + 1, 2):
#        if nm % i == 0:
#            primo = False
#        break
#    if primo:
#        print("É primo")
#    else:
#        print("Não é primo")

#ex8
#num = input("Digite uma lista de números com espaço: ").split()
#num = [int(x) for x in num]

#numeros_n_rep = sorted(set(num))
#print("Os números nao duplicados e em ordem crescente: ", numeros_n_rep)

#Ex9
#ent = input("Digite uma lista de números inteiros separados por espaços: ")
#numeros = []
#for nm in ent.split():
#   numeros.append(int(nm))

#soma = 0
#for nm in numeros:
#    soma += nm
#media = soma / len(numeros)

#acima_media = []
#for nm in numeros:
#    if nm > media:
#        acima_media.append(nm)

#print(f"Média dos numeros pares: {media:.2f}")
#print(f"Números acima da média: ", acima_media)


#ex13
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
            break


#ex15
#def encontrar_maior(lista):
#    maior = 0 
#    for numero in lista:
#        if numero > maior:
#            maior = numero
#            return maior

#entrada = input("Digite uma lista de números separados por espaço: ")
#numeros = list(map(int, entrada.split()))

#maior_numero = max(numeros)
#print("O maior número da lista é: ", maior_numero)

#encontrar_maior

#Erro no print