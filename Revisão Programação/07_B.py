n = int(input())
valores = 0
for i in range(1, n+1):
    soma_total = 1/i
    valores += soma_total

print(f'{valores:.4f}')