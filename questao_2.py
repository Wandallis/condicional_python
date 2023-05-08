#2. Faça um programa que receba um número e imprima se o número é par ou ímpar.

numb = int(input("digite o numero:"))
numb1 = numb % 2
if numb1 == 0 :
    print("O número é par!")
else:
    print("O número é ímpar!")
    
