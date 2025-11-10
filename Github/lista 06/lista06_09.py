def lista_troca_menor_primeiro(lista):
    if len(lista) < 2:
        return 0
    indice_menor = 0
    for i in range(1, len(lista)):
        if lista[i] < lista[indice_menor]:
            indice_menor = i
    if indice_menor == 0:
        return 0
    else:
        lista[0], lista[indice_menor] = lista[indice_menor], lista[0]
        return 1