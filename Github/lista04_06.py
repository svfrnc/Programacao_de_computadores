nota_11 , nota_21 = map(int , input().split())
nota_12 , nota_22 = map(int , input().split())
p1 , p2 = map(int, input().split())
media_01 = ((nota_11 * p1) + (nota_21 * p2)) // (p1 + p2)
media_02 = ((nota_12 * p1) + (nota_22 * p2)) // (p1 + p2)
if media_01 >= media_02:
    print('1')
else:
    print ('2')