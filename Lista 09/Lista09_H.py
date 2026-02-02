def main():
    try:
        linha1 = input().split()
        if not linha1:
            return
        n = int(linha1[0])
        
        linha2 = input().split()
        sequencia = list(map(int, linha2))
    except EOFError:
        return

    if n <= 2:
        print(1)
        return
    qtd_escadinhas = 1

    diferenca_atual = sequencia[1] - sequencia[0]

    for i in range(2, n):

        nova_diferenca = sequencia[i] - sequencia[i-1]

        if nova_diferenca != diferenca_atual:
            qtd_escadinhas += 1
            diferenca_atual = nova_diferenca
    print(qtd_escadinhas)

if __name__ == "__main__":
    main()