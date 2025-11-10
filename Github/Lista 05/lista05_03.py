A=int(input())
B=int(input())
C=int(input())
distancia_AB = B - A
distancia_bc = C - B
if distancia_AB < distancia_bc:
    print('1')
elif distancia_AB > distancia_bc:
    print ('-1')
else:
    print('0')