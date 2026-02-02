def reduzir_a_um_algarismo(numero_str):
    while len(numero_str) > 1:
        soma = 0
        for digito in numero_str:
            soma += int(digito)
        numero_str = str(soma)
    return int(numero_str)

def main():
    while True:
        try:
            entrada = input().split()
            
            if not entrada:
                break
                
            n_str = entrada[0]
            m_str = entrada[1]
            if n_str == '0' and m_str == '0':
                break
            valor_n = reduzir_a_um_algarismo(n_str)
            valor_m = reduzir_a_um_algarismo(m_str)

            if valor_n > valor_m:
                print(1)
            elif valor_m > valor_n:
                print(2)
            else:
                print(0)
                
        except EOFError:
            break

if __name__ == "__main__":
    main()