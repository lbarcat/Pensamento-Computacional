import random

ERR = 'ausente'

lista = []
mostra = ''

n = int(input('\nn: '))
for i in range(n):
    ichave = int((random.random() * 99) % 100)
    schave = str(ichave)
    lista.append(ichave)
lista.sort()
print(lista)

chave = int(input('chave:'))
print()

esq = 0
dir = len(lista) - 1
ind = -1

while esq <= dir:
    meio = (esq + dir) // 2
    conteudo = lista[meio]
    print('meio:', meio, 'contém:', conteudo)
    if conteudo == chave:
        ind = meio
        break
    elif conteudo > chave:
        dir = meio - 1
    else: 
        esq = meio + 1
            
if ind == -1:
    print(ERR)
else:
    print('\níndice:', ind)
  