# Faça um programa que receba dois números e mostre na tela qual é o maior, ou se são iguais.

n1 = int(input("Escreva o primeiro número: "))
n2 = int(input("Escreva o segundo número: "))

if n1 == n2:
    print("Iguais!")
elif n1 > n2:
    print(f"{n1} é o maior")
else:
    print(f"{n2} é o maior")