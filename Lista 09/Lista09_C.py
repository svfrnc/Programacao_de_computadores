n = int(input())
interruptor = []
acesa = 0
ultima_lampada = 0
for i in range(n):
    x = int(input())
    interruptor.append(x)
    if i > 1:
        acesa += 1
if interruptor[-1] > 1:
    ultima_lampada += 1

print(acesa)
print(ultima_lampada)



