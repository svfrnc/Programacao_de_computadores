comprimento_estrada , distancia_pedagios = map(int,input().split())
custo_km , valor_pedagio = map(int,input().split())
quantidade_pedagios = comprimento_estrada//distancia_pedagios
valor_km= comprimento_estrada*custo_km
preco_total_pedagio= quantidade_pedagios*valor_pedagio
total_pagar=valor_km+preco_total_pedagio
print(total_pagar)