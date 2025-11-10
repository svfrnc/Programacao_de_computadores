capacidade_cabine = int(input())
total_alunos = int(input())
total_viagens = total_alunos // (capacidade_cabine - 1)
if (total_alunos % (capacidade_cabine - 1)) > 0:
    print(total_viagens+1)
else:
    print(total_viagens)