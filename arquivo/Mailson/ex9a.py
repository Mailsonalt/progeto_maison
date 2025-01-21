ent = input("Digite uma lista de números inteiros separados por espaços: ")
numeros = []
for nm in ent.split():
   numeros.append(int(nm))

soma = 0
for nm in numeros:
    soma += nm
media = soma / len(numeros)

acima_media = []
for nm in numeros:
    if nm > media:
        acima_media.append(nm)

print(f"Média dos numeros pares: {media:.2f}")
print(f"Números acima da média: ", acima_media)
