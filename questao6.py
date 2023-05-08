#6. Faça um programa que leia 3 notas, verique se as notas são válidas e exiba na tela a média destas notas com duas casas decimais. Uma nota válida deve ser, obrigatoriamente, um valor entre 0.00 e 10.00, onde caso a nota não possua valor válido, este fato deve ser informado ao usuário e o programa termina.

p = 'S'
while p == 'S':
    n1 = float(input("digite o numero 1:"))
    n2 = float(input("digite o numero 2:"))
    n3 = float(input("digite o numero 3:"))
    numb = 0
    
    if 0 < n1 < 10 and 0 < n2 < 10 and 0 < n3 < 10 :
        numb = n1
        numb += n2
        numb += n3
        media = (n1+n2+n3)/3
        print("A média será: %.2f" %media)
    else: 
        print("invalido")
    p = str(input("voce deseja continuar? (digite S ou N)"))
print("FIM!")




