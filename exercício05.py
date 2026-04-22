print("São múltiplos ou não?")

n1 = float(input("Digite o 1º número: "))
n2 = float(input("Digite o 2º número: "))

divisao = n1 / n2

if n1 % n2 == 0:
    print(f"Resultado da divisao: {divisao}")
    print(f"O {n1} e o {n2} são múltiplos.")
else:
    print(f"Resultado da divisao: {divisao}")
    print(f"O {n1} e o {n2} não são múltiplos.")