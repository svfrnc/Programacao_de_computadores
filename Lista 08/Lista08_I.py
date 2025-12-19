caso = 1
while True:
    try:
        linha = input()
        if not linha:
            break
        n = int(linha)
        
        valores = input().split()
        
        lista = []
        for i in range(10):
           
            lista.append([float(valores[i]), i])
            

        for i in range(10):
            for j in range(9):
                oleo_atual = lista[j][0]
                digito_atual = lista[j][1]
                
                oleo_proximo = lista[j+1][0]
                digito_proximo = lista[j+1][1]
                trocar = False
                if oleo_proximo > oleo_atual:
                    trocar = True
                elif oleo_proximo == oleo_atual:
                    if digito_proximo < digito_atual:
                        trocar = True
                
                if trocar:
                    temp = lista[j]
                    lista[j] = lista[j+1]
                    lista[j+1] = temp
        
        senha = ""
        for i in range(n):
            digito = lista[i][1]
            senha += str(digito)
            
        print(f"Caso {caso}: {senha}")
        caso += 1
        
    except EOFError:
        break