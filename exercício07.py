print("Voto obrigatório em 2026")
ano_nascimento = int(input("Informe o ano do seu nascimento: "))

voto = 2026 - ano_nascimento

if voto > 70:
    print("O voto é opicional")
elif voto >= 18:
    print("O voto é obrigatório")
elif voto >= 16:
    print("O voto é opicional")
else:
    print("O voto é proibido")