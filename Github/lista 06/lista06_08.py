def media_lista(lista):
    soma_total = 0
    qntd_elementos = 0
    for numero in lista:
        soma_total = soma_total + numero
        qntd_elementos = qntd_elementos + 1
    media_final = soma_total // qntd_elementos
    return media_final