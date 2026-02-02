def main():
    while True:
        try:
            frase = input()
            
            if frase == '*':
                break

            palavras = frase.split()

            if not palavras:
                continue
            letra_referencia = palavras[0][0].lower()
            
            eh_tautograma = True
            for palavra in palavras:
                if palavra[0].lower() != letra_referencia:
                    eh_tautograma = False
                    break
            if eh_tautograma:
                print('Y')
            else:
                print('N')

        except EOFError:
            break

if __name__ == "__main__":
    main()