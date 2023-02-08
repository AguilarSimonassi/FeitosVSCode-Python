# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

slr = int(input("Qual seu salário ? "))

if slr <= 280:
    reaj = slr * 20 / 100
    aumento = reaj + slr
    print("Salário antes do reajuste: ", slr)
    print("Percentual de aumento: ", "20%")
    print("O valor do aumento aplicado: ", reaj)
    print("O novo salario: ", aumento)
elif slr > 280 and slr <= 700:
    reaj = slr * 15 / 100
    aumento = reaj + slr
    print("Salário antes do reajuste: ", slr)
    print("Percentual de aumento: ", "15%")
    print("O valor do aumento aplicado: ", reaj)
    print("O novo salario: ", aumento)
    print("Nada")
elif slr > 700 and slr <= 1500:
    reaj = slr * 10 / 100
    aumento = reaj + slr
    print("Salário antes do reajuste: ", slr)
    print("Percentual de aumento: ", "10%")
    print("O valor do aumento aplicado: ", reaj)
    print("O novo salario: ", aumento)
else:
    reaj = slr * 5 / 100
    aumento = reaj + slr
    print("Salário antes do reajuste: ", slr)
    print("Percentual de aumento: ", "5%")
    print("O valor do aumento aplicado: ", reaj)
    print("O novo salario: ", aumento)

    