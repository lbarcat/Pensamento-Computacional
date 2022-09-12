import random

lista = []
n = int(input('\nn: '))
for i in range(n):
    ichave = int((random.random() * 99) % 100)
    lista.append(ichave)

print(lista)

for i in range(len(lista)):
    menor = i
    aux = lista[i]
    for j in range(i + 1, len(lista)):
        if lista[j] < lista[menor]:
            menor = j
    if lista[i] != lista[menor]:
        aux = lista[i]
        lista[i] = lista[menor]
        lista[menor] = aux
        print('trocou {:3} por {:3}\n'.format(aux, lista[i]))
    else:
        print('não trocou\n')
    print(lista)
