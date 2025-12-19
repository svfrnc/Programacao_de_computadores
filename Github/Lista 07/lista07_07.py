n = int(input()) 
qtd = list(map(int, input().split()))
lista_maior = []
lista_menor = []

media = sum(qtd) / n
for i in qtd:
    if i < media:
        lista_menor.append(i) 
    if i >= media:
        lista_maior.append(i)

print(f'{media:.1f}')
print(len(lista_menor), *lista_menor) 
print(len(lista_maior), *lista_maior)
