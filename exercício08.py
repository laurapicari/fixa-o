salario = float(input("Informe o salário: "))

if salario > 1500:
    resultado4 = salario * 5/100
    ajuste4 = salario + resultado4
    print(f"""Salário antes do ajuste:{salario}
    Porcentagem de aumento: 5%
    Valor do aumento:R${resultado4}
    Novo salário:{ajuste4}""")
elif salario >= 700:
    resultado1 = salario * 10/100
    ajuste1 = salario + resultado1
    print(f"""
    Salário antes do ajuste:{salario}
    Porcentagem de aumento: 10%
    Valor do aumento:R${resultado1}
    Novo salário:{ajuste1}""")
elif salario >= 280:
        resultado2 = salario * 15 / 100
        ajuste2 = salario + resultado2
        print(f"""
        Salário antes do ajuste:{salario}
        Porcentagem de aumento: 15%
        Valor do aumento:R${resultado2}
        Novo salário:{ajuste2}""")
elif salario >= 280:
    resultado3 = salario * 20/100
    ajuste3 = salario + resultado3
    print(f"""
    Salário antes do ajuste:{salario}
    Porcentagem de aumento: 20%
    Valor do aumento:R${resultado3}
    Novo salário:{ajuste3}""")
else:
    resultado5 = salario * 20 / 100
    ajuste5 = salario + resultado5
    print(f"""
    Salário antes do ajuste:{salario}
    Porcentagem de aumento: 20%
    Valor do aumento:R${resultado5}
    Novo salário:{ajuste5}""")

