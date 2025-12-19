def somar_lista(lista):
    # 1. CASO BASE: Se a lista estiver vazia, retornamos 0
    if len(lista) == 0:
        return 0
    
    # 2. CASO RECURSIVO: 
    # Retorne o primeiro item somado à função chamando o resto da lista
    else:
        return lista[0] + somar_lista(lista[1:])

# Teste
meus_numeros = [2, 4, 6, 8]
resultado = somar_lista(meus_numeros)
print(resultado) # Deve imprimir 20