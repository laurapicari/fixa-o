nome = input("Digite o nome do aluno: ")

print(f"Média do aluno {nome}:")

nota1 = float(input("1ª nota: "))
nota2 = float(input("2ª nota: "))
nota3 = float(input("3ª nota: "))
nota4 = float(input("4ª nota: "))

media = (nota1 + nota2 + nota3 + nota4)/4

print(f"Média:{media}")

if media >= 7:
    print("Aprovado")
elif media <= 4:
    print("Reprovado")
elif media <= 6:
    print("Em recuperação")

print("FIM")