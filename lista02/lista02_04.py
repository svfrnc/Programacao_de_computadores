valor_item=int(input())
quantidade=int(input())
valor_pago=int(input())
valor_final=(valor_item*quantidade)
troco=valor_pago-valor_final
print(f'A pagar: {valor_final}')
print(f'Troco  : {troco}')