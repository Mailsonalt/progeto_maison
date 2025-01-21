nm = int(input("Digite um número inteiro positivo: "))
if nm <= 1:
    print("Não é primo")
elif nm == 2:
    print("É primo")
elif nm % 2 == 0:
    print("Não é primo")
else:
    primo = True
    for i in range(3, int(nm ** 0.5) + 1, 2):
        if nm % i == 0:
            primo = False
        break
    if primo:
        print("É primo")
    else:
        print("Não é primo")
