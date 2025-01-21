num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))

if num1 and num2 == num3:
    print("Esta forma geométrica é equilátera")
elif num1 or num2 == num3:
    print("Forma geométrica Isóceles")
else:
    print("forma geométrica escaleno")