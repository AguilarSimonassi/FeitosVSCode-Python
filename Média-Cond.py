# Faça a média de três notas e diga se foi aprovado, reprovado ou está em recuperação

print("Digite as 3 médias: ")
n1 = float(input("nota1: "))
n2 = float(input("nota2: "))
n3 = float(input("nota3: "))

media = (n1 + n2 + n3) / 3
print(f"Média: {media:.2f}")

if media >= 6:
    print("Aprovado!")
elif media < 6 and media >= 4:
    print("Recuperação!")
else:
    print("Reprovado!")