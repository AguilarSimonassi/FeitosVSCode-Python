# Faça um Programa que leia três números e mostre o maior deles.

n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
n3 = int(input("Número 3: "))

if n1 > n2 and n1 > n3:
    print(f"O maior é o número 1 - {n1}")
elif n2 > n1 and n2 > n3:
    print(f"O maior é o número 2 - {n2}")
else:
    print(f"O maior é o número 3 - {n3}")