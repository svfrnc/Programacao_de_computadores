N = int(input())
valor_conta = 0
if N <= 10:
    valor_conta = 7
elif N <= 30:
    valor_conta = 7 + (N - 10) * 1
elif N <= 100:
    valor_conta = 7 + 20 + (N - 30) * 2
else: 
    valor_conta = 7 + 20 + 140 + (N - 100) * 5
print(valor_conta)