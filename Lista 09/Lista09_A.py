def main():
    entrada_linha1 = input().split()
    J = int(entrada_linha1[0])
    R = int(entrada_linha1[1])

    pontos = list(map(int, input().split()))

    placar_jogadores = [0] * J

    for i in range(len(pontos)):

        jogador_atual = i % J
        
        placar_jogadores[jogador_atual] += pontos[i]

    melhor_pontuacao = -1
    vencedor = -1

    for i in range(J):

        if placar_jogadores[i] >= melhor_pontuacao:
            melhor_pontuacao = placar_jogadores[i]
            vencedor = i + 1  
    print(vencedor)

if __name__ == "__main__":
    main()