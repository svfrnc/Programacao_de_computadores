d = int(input())
h , l , p = map(int,input().split())
if d <= h and d <= l and d <= p:
    print("S")
else:
    print("N")