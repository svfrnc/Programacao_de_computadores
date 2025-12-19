n = int(input())
candidato = n + 1

while True:
    primo = True
    if candidato <= 1:
        primo = False
    else:
        limite = int(candidato ** 0.5)
        for i in range(2, limite + 1):
            if candidato % i == 0:
                primo = False
                break
    
    if primo:
        print(candidato)
        break
    candidato += 1