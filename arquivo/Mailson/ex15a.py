def encontrar_maior(lista):
    maior = 0 
    for numero in lista:
        if numero > maior:
            maior = numero
            return maior

entrada = input("Digite uma lista de números separados por espaço: ")
numeros = list(map(int, entrada.split()))

maior_numero = max(numeros)
print("O maior número da lista é: ", maior_numero)

encontrar_maior

#Erro no print