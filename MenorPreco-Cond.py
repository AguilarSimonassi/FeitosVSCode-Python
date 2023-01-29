# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve 
# comprar, sabendo que a decisão é sempre pelo mais barato.

p1 = float(input("Preço do primeiro produto: "))
p2 = float(input("Preço do segundo produto: "))
p3 = float(input("Preço do terceiro produto: "))

if p1 < p2 and p1 < p3:
    print("Melhor produto a se comprar é: Produto 1")
elif p2 < p1 and p2 < p3:
    print("Melhor produto a se comprar é: Produto 2")
else:
    print("Melhor produto a se comprar é: Produto 3")
