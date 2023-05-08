
#3. Ler 4 números inteiros e calcular a soma dos que forem par.

n1 = int(input("digite o numero 1:"))
n2 = int(input("digite o numero 2:"))
n3 = int(input("digite o numero 3:"))
n4 = int(input("digite o numero 4:"))

soma = 0
if n1%2 == 0 :
    soma = n1
if n2%2 == 0 :
    soma += n2
if n3%2 == 0 :
    soma += n3
if n4%2 == 0 :
    soma += n4

print("O valor da soma dos numeros pares será {}" .format(soma))
