print("Calculadora simples:")

n1 = float(input("Digite o 1º número: "))
n2 = float(input("Digite o 2º número: "))

escolha_usuario = int(input("""
1 - soma
2 - subtração
3 - multiplicação
4 - divisão
Escolha a operação que deseja: """))

match escolha_usuario:
    case 1:
        resultado1 = n1 + n2
        print(f"Resultado: {resultado1}")
    case 2:
        resultado2 = n1 - n2
        print(f"Resultado: {resultado2}")
    case 3:
        resultado3 = n1 * n2
        print(f"Resultado: {resultado3}")
    case 4:
        resultado4 = n1 / n2
        print(f"Resultado: {resultado4}")