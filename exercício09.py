estado = float(input("Informe o estado de origem(1-5): "))
peso_ton = int(input("Informe o peso em toneladas: "))
codigo = int(input("Informe o código de carga(10-40): "))

peso_quilos = peso_ton * 1000

#imposto
match estado:
    case 1:
        imposto = peso_quilos * 20/100
    case 2:
        imposto = peso_quilos * 15/100
    case 3:
        imposto = peso_quilos * 10/100
    case 4:
        imposto = peso_quilos * 5/100
    case 5:
        imposto = 0


if codigo <= 10:
    preco_kg1 = 100
    preco_carga1 = peso_quilos * preco_kg1
    valor_imposto1 = preco_carga1 * imposto
    valor_total1 = preco_carga1 + imposto
    print(f"""Resultados:
    Peso da carga: {peso_quilos:.2f} kg
    Preço da carga: R$ {preco_carga1:,.2f}
    Imposto R$: {valor_imposto1:,.2f}
    Valor total transportado: R$ {valor_total1:,.2f}""")

elif codigo <= 21:
    preco_kg2 = 250
    preco_carga2 = peso_quilos * preco_kg2
    valor_imposto2 = preco_carga2 * imposto
    valor_total2 = preco_carga2 + imposto
    print(f"""Resultados:
    Peso da carga: {peso_quilos:.2f} kg
    Preço da carga: R$ {preco_carga2:,.2f}
    Imposto R$: {valor_imposto2:,.2f}
    Valor total transportado: R$ {valor_total2:,.2f}""")

else:
    preco_kg3 = 340
    preco_carga3 = peso_quilos * preco_kg3
    valor_imposto3 = preco_carga3 * imposto
    valor_total3 = preco_carga3 + imposto
    print(f"""Resultados:
    Peso da carga: {peso_quilos:.2f} kg
    Preço da carga: R$ {preco_carga3:,.2f}
    Imposto R$: {valor_imposto3:,.2f}
    Valor total transportado: R$ {valor_total3:,.2f}""")



