n = int(input())

contador = 0

# verificação se o valor do input é maior que 1
if n == 1:
    print ('Nao')
else:
# funçao para verificar valor primo
    for i in range(2, n):
        if n % i == 0:
            contador += 1
# verificador dos valores divisiveis possíveis
    if contador > 0:
            print ('Nao')
    else:
            print('Sim')
