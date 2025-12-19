a , b = map(int,input().split())

#função que divide o valor dentro da lista com o valor de b
for i in range(1 , b + 1):
    if i % a == 0:
        print(i, end=" ")
    
