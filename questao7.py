#7. Leia o salário de um trabalhador e o valor da prestação de um empréstimo.
#Se a prestação for maior que 20% do salário então imprima: Empréstimo não concedido, caso contrário imprima: Empréstimo concedido.


p = 'S'
while p == 'S':
    s = float(input("digite o valor do salário:"))
    p = float(input("digite o valor da prestação:"))
    
    if (s*0.20) > p:
        print("empréstimo concedido!")
    else: 
        print("empréstimo não concedido")
    p = str(input("voce deseja continuar? (digite S ou N)"))
print("FIM)
