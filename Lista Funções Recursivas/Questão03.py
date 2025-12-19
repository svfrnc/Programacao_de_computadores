def potencia (base,expoente):
    if expoente ==0:
        return 1
    elif expoente ==1:
        return base
    else:
        return base * potencia (base, expoente -1)
