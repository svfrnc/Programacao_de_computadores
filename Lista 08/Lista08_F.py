while True:
    valores = input().split()
    h1 = int(valores[0])
    m1 = int(valores[1])
    h2 = int(valores[2])
    m2 = int(valores[3])
    if h1 == 0 and m1 == 0 and h2 == 0 and m2 == 0:
        break
    inicio_em_minutos = (h1 * 60) + m1
    fim_em_minutos    = (h2 * 60) + m2

    total_minutos = fim_em_minutos - inicio_em_minutos
    
    if total_minutos < 0:
        total_minutos = total_minutos + 1440
        
    print(total_minutos)