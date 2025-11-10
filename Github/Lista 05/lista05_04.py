idade_monica = int(input())
idade_filho01 = int(input())
idade_filho02 = int(input())

idade_filho03 = idade_monica - (idade_filho01 + idade_filho02)

if idade_filho01 >= idade_filho02 and idade_filho01 >= idade_filho03:
    print(idade_filho01)
elif idade_filho02 >= idade_filho03:
    print(idade_filho02)
else:
    print(idade_filho03)