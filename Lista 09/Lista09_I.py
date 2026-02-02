def main():
    num_teste = 1
    
    while True:
        try:
            linha = input().split()
            if not linha:
                continue
            
            n = int(linha[0])

            if n == 0:
                break
            inter_x, inter_y, inter_u, inter_v = None, None, None, None
            for _ in range(n):
                x, y, u, v = map(int, input().split())
                
                if inter_x is None:
                    inter_x, inter_y, inter_u, inter_v = x, y, u, v
                else:
                    inter_x = max(inter_x, x)
                    inter_y = min(inter_y, y)
                    inter_u = min(inter_u, u)
                    inter_v = max(inter_v, v)
            print(f"Teste {num_teste}")
            if inter_x < inter_u and inter_v < inter_y:
                print(f"{inter_x} {inter_y} {inter_u} {inter_v}")
            else:
                print("nenhum")
                
            print()
            
            num_teste += 1

        except EOFError:
            break

if __name__ == "__main__":
    main()