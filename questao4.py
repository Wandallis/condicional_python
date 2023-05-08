#4. Ler três valores e determinar o maior entre eles.

p = 'S'
while p == 'S':
    n1 = int(input("digite o numero 1:"))
    n2 = int(input("digite o numero 2:"))
    n3 = int(input("digite o numero 3:"))
    if n1 > n2 and n1 > n3  :
        print("O número {} é maior que {} e {}" .format(n1,n2,n3)) 
    elif n2 > n1 and n2 > n3  :
        print("O número {} é maior que {} e {}" .format(n2,n1,n3)) 
    else :
        print("O número {} é maior que {} e {}" .format(n3,n2,n1)) 
    p = str(input("voce deseja continuar? (digite S ou N"))
print("FIM")

