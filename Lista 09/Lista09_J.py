def main():
    try:
        line = input().split()
        if not line:
            return
        n = int(line[0])
        
        line = input().split()
        k = int(line[0])
        
        notas = []
        for _ in range(n):
            line = input().split()
            notas.append(int(line[0]))
            
        notas.sort(reverse=True)
        
        nota_corte = notas[k-1]
        
        classificados = 0
        for nota in notas:
            if nota >= nota_corte:
                classificados += 1
            else:
                break
        print(classificados)
        
    except EOFError:
        pass

if __name__ == "__main__":
    main()