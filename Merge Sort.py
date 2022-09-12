import random

def mesclar(lesq, ldir):
  print('mesclar:', lesq,'+', ldir)
  # lesq tem mais que um elemento?
  if len(lesq) == 0:
      return ldir
  # ldir tem mais que um elemento?
  if len(ldir) == 0:
      return lesq

  #Faça lista vazia mescla
  # Faça ind_esq → 0
  # Faça ind_dir → 0
  mescla = []
  ind_esq = 0
  ind_dir = 0

  #mescla contém todos os elementos de lesq e ldir ?
  while len(mescla) < len(lesq) + len(ldir):
    #lesq[ind_esq] é menor ou igual a ldir[ind_dir]? 
    if lesq[ind_esq] <= ldir[ind_dir]:
      # Anexe esq[ind_esq] a mescla
      #  Avance ind_esq
      mescla.append(lesq[ind_esq])
      ind_esq += 1
      # ind_esq chegou ao fim de esq?
      if ind_esq == len(lesq):
        # Anexe o restante de ldir a mescla
        mescla += ldir[ind_dir:]
    else:
      # Anexe ldir[ind_dir] a mescla
      # Avance ind_dir
      mescla.append(ldir[ind_dir])
      ind_dir += 1
      # ind_dir chegou ao fim de ldir?
      if ind_dir == len(ldir):
        # Anexe o restante de lesq a mescla
        mescla += lesq[ind_esq:]
          
  print('mesclada:', mescla)
  return mescla

def merge_sort(lista):
  print('dividir:', lista)
  # lista tem mais que um elemento?
  if len(lista) < 2:
      return lista

  meio = len(lista) // 2
  # Divida lista em duas metades: lista_esq e lista_dir
  lesq = lista[:meio]
  ldir = lista[meio:]
  lesq = merge_sort(lesq)
  ldir = merge_sort(ldir)
  # lesq = merge_sort(lista[:meio])
  # ldir = merge_sort(lista[meio:])
  return mesclar(lesq, ldir)

  
lista = []
n = int(input('\nn: '))
for i in range(n):
    ichave = int((random.random() * 99) % 100)
    lista.append(ichave)

print('original:',lista)

lord = merge_sort(lista)

print('ordenada:',lord)
