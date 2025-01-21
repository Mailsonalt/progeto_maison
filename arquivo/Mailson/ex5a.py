def eh_palindromo(palavra):
    palavra = palavra.lower().replace(" ", "")
    return palavra == palavra[::-1]
palavra = input("Digite uma frase: ")
print(palavra[::-1])

if eh_palindromo(palavra):
    print("A palavra é um palindromo")
else:
    print("A palavra não é um palindromo")
eh_palindromo
