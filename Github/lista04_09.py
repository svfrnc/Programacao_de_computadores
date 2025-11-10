A , B , C = map(int,input().split())
if (A + B > C) and (A + C > B) and (B + C > A):
    if A >= B and A >= C:
        if B**2 + C**2 == A**2:
            print('r')
        elif B**2 + C**2 > A**2:
            print('a')
        else:
            print('o')
    elif B >= A and B >= C:
        if A**2 + C**2 == B**2:
            print('r')
        elif A**2 + C**2 > B**2:
            print('a')
        else:
            print('o')
    else:
        if A**2 + B**2 == C**2:
            print('r')
        elif A**2 + B**2 > C**2:
            print('a')
        else:
            print('o')            
else:
    print('n')