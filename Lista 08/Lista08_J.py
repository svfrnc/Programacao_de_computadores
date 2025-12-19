entrada = input().split()
n = int(entrada[0])
r = int(entrada[1])


voltou = list(map(int, input().split()))


checklist = [False] * (n + 1)

for mergulhador in voltou:
    checklist[mergulhador] = True


encontrou_falta = False


for i in range(1, n + 1):

    if checklist[i] == False:

        print(i, end=" ")
        encontrou_falta = True
if not encontrou_falta:
    print("*")
else:
    print()