n = int(input())
# valor de acumulação da recursividade
acumulador = 0
# para cada valor dentro do alcance da função, realizar a divisão deste pelo input
for i in range (1, n + 1):
    somatorio = 1 / i
    acumulador += somatorio
print (f'{acumulador:.4f}')