#5. Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do
número. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.

p = 'S'
while p == 'S':
    n1 = float(input("digite o numero 1:"))
    if n1 > 0:
        raiz = n1**(1/2)
        print("O valor do quadrado será: %.2f" %raiz)
    else:
        print("o numero é invalido!")
    p = str(input("voce deseja continuar? (digite S ou N)"))
print("FIM!")

