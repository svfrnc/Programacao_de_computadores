t = int(input())

for i in range(t):
    linha1 = input().split()
    dinheiro = float(linha1[0])
    n = int(linha1[1])

    lista_precos = input().split()
    maior_troco = 0.0
    primeiro_valido = True
    
    for p in lista_precos:
        preco = float(p)
    
        qtd = int(dinheiro / preco)
        if qtd > 0:
            custo_total = qtd * preco
            troco_atual = dinheiro - custo_total
        
            if primeiro_valido:
                maior_troco = troco_atual
                primeiro_valido = False
            elif troco_atual > maior_troco:
                maior_troco = troco_atual
    print(f"{maior_troco:.2f}")