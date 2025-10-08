NOME=input()
salario_base=float(input())
vendas_mensais=float(input())
acrescimo_salario = (vendas_mensais*(15/100))
salario_final= acrescimo_salario+salario_base
print(NOME)
print(f"R$ {salario_final:.2f}")