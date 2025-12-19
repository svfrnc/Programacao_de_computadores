n = int(input())

for i in range(n):
    c = float(input())
    dias = 0
    while c > 1.0:
        c = c / 2 
        dias += 1 
    print(f"{dias} dias")