def main():
    mensagem = input()
    crib = input()

    m_len = len(mensagem)
    c_len = len(crib)

    contagem_posicoes = 0
    for i in range(m_len - c_len + 1):
        
        posicao_valida = True 
        for j in range(c_len):
            if mensagem[i + j] == crib[j]:
                posicao_valida = False
                break  
        if posicao_valida:
            contagem_posicoes += 1
    print(contagem_posicoes)

if __name__ == "__main__":
    main()