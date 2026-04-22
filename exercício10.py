a = float(input("Informe o valor do 1º lado: "))
b = float(input("Informe o valor do 2º lado: "))
c = float(input("Informe o valor do 3º lado: "))

if a >= b + c:
    print("Não forma triângulo")
elif a**2 == (b**2 + c**2):
    print("Triângulo retângulo")
elif a**2 > (b**2 + c**2):
    print("Triângulo obtusângulo")
elif a ** 2 < (b ** 2 + c ** 2) and a == b == c:
    print("Triângulo acutângulo, equilátero")
elif a**2 < (b**2 + c**2) and a != b == c:
    print("Triângulo acutângulo, isósceles")
elif a == b != c:
    print("Triângulo isósceles")
elif a != b == c:
    print("Triângulo isósceles")
