n = int(input())
batimentos = []
 
for i in range(n):
    x = int(input())
    batimentos.append(x)

media = sum(batimentos) // n
fora_media = 0
limite_abaixo = int(media * 0.9)
limite_acima = int(media * 1.1)


for b in batimentos:
    if b < limite_abaixo or b > limite_acima:
        fora_media += 1
        
print(media)
print(fora_media)
