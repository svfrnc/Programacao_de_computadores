valorL_alcool , valorL_gasolina , rendimento_alcool , rendimento_gasolina = map(float, input().split())
if (valorL_alcool / rendimento_alcool) < (valorL_gasolina / rendimento_gasolina):
    print('A')
else:
    print('G') 