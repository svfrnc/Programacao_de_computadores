Ca, Ba, Pa = map(int, input().split())
Cr, Br, Pr = map(int, input().split())
nao_atendidos = 0
if Cr > Ca:
    nao_atendidos += Cr - Ca
if Br > Ba:
    nao_atendidos += Br - Ba
if Pr > Pa:
    nao_atendidos += Pr - Pa
print(nao_atendidos)