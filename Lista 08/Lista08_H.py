while True:
    try:
        linha = input()
        if not linha: break 
        
        n = int(linha)
        
        if n == 0:
            break
            
        magnitudes = list(map(int, input().split()))
        
        picos = 0
        for i in range(n):
            atual = magnitudes[i]
            
            anterior = magnitudes[i-1]
            
            proximo = magnitudes[(i+1) % n]
            
            if atual > anterior and atual > proximo:
                picos += 1
            elif atual < anterior and atual < proximo:
                picos += 1
                
        print(picos) 
    except EOFError:
        break