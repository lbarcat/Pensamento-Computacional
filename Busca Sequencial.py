import random

ERR = 'ausente'

lista = []
mostra = ''

n = int(input('\nn: '))
for i in range(n):
    ichave = int((random.random() * 99) % 100)
    schave = str(ichave)
    lista.append(ichave)
    mostra += schave + ' '
print(mostra)
chave = int(input('\nbuscar: '))
print()
resp = ''

ind = -1

for i in range(len(lista)):
    j = lista[i]
    resp += str(j) + ' '
    if j == chave:
        ind = i
        break
    else:
        print(resp)
if ind == -1:
    print(ERR)
else:
    print(resp, '\níndice:', ind)
