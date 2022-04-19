# Miguel Angel Sarmiento Aguiar
# Marlon Perez Rios

# Punto 1.1

import timeit

def insertionSort(array):
  temp = 0
  j = 0
  for i in range(len(array)):
    j = i
    while ((j > 0) and (array[j-1] > array[j])):
      temp = array[j]
      array[j] = array[j-1]
      array[j-1] = temp
      j = j-1
  return array

Lista = list(range(10000))
Lista = Lista[::-1]

Start = timeit.default_timer()
print(insertionSort(Lista))
Stop = timeit.default_timer()
print('Time:', Stop-Start)

# Punto 1.2

import timeit

def mergeSort(a):
  tmp = [None]*len(a)
  mergeSortAux(a, tmp,  0,  len(a)-1)
  print(a)

def mergeSortAux(a, tmp, left, right):
  if (left < right):
    center = (left+right)//2
    mergeSortAux(a, tmp, left, center)
    mergeSortAux(a, tmp, center+1, right)
    merge(a, tmp, left, center+1, right)

def merge(a, tmp, left, right, rightEnd):
  leftEnd = right-1
  k = left
  num = rightEnd-left+1
  while ((left <= leftEnd) and (right <= rightEnd)):
    if (a[left] <= a[right]):
      tmp[k] = a[left]
      k = k+1
      left = left+1
    else:
      tmp[k] = a[right]
      k = k+1
      right = right+1
  while (left <= leftEnd):
    tmp[k] = a[left]
    k = k+1
    left = left+1
  while(right <= rightEnd):
    tmp[k] = a[right]
    k = k+1
    right = right+1
  for i in range(num):
    a[rightEnd] = tmp[rightEnd]
    rightEnd = rightEnd-1

Lista = list(range(10000))
Lista = Lista[::-1]

Start = timeit.default_timer()
mergeSort(Lista)
Stop = timeit.default_timer()
print('Time:', Stop-Start)
