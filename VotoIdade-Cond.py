# Faça um programa que receba o ano de nascimento, o
# ano atual e calcule a idade do usuário. Mostre na tela qual a categoria de voto ele se encontra segundo a tabela.
# - Abaixo de 16: Não Vota
# - Entre 16 e 18: Voto Facultativo
# - Entre 18 (incluso) e 60 (incluso): Voto Obrigatorio
# - Acima de 60: Voto Facultativo

anonasci = int(input("Qual o ano de nascimento: "))
anoatual = int(input("Digite o ano atual: "))

idade = anoatual - anonasci

print(f"Sua idade é: {idade}")

if idade < 16:
    print("Não vota!")
elif idade >= 16 and idade < 18:
    print("Voto Facultativo!")
elif idade >= 18 and idade <= 60:
    print("Voto Obrigatorio!")
else:
    print("Voto Facultativo!")
