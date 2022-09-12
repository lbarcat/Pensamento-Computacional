import random

lista = []
n = int(input('\nn: '))
for i in range(n):
    ichave = int((random.random() * 99) % 100)
    lista.append(ichave)


for i in range(len(lista)):
  item = lista[i]
  print('processando', item)
  j = i - 1
  while j >= 0 and lista[j] > item:
    lista[j + 1] = lista[j]
    j -= 1
    print(item, '->', lista)
  lista[j + 1] = item  
  print(lista,'\n')
