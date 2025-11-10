a , b , c , d = map(int, input().split())
if (a+b) >c and (a+c)>b and (b+c) > a:
    print('S')
elif (a+d) > b and (b+d) > a and (a+b) > d:
    print('S')
elif (a+c) > d and (d+c)>a and (a+d)>c:
    print('S')
elif (b+c) > d and (d+c)>b and (b+d)>c:
    print('S')
else:
    print ('N')