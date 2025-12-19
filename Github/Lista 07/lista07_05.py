n = int(input())
qtd = list(map(int,input().split()))

#media dos valores
media = sum(qtd) / n
menor = 0
maior = 0
#valores acima da media
for i in qtd:
    if i < media:
        menor += 1
    if i >= media:
        maior += 1
print (f'{media:.1f}')
print(menor)
print(maior)