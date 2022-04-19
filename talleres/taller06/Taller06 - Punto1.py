# Punto 1

# Miguel Angel Sarmiento Aguiar
# Marlon Perez Rios

import numpy

class ArrayList():

  def __init__(self):
    self.defaultSize = 10
    self.elements = numpy.empty(self.defaultSize, dtype=object)
    self.size = 0

  def size(self):
    return self.size

  def get(self, index):
    if ((index < self.size) and (index >= 0)):
      return self.elements[index]
    else:
      raise Exception("Index out of bounds")

  def add(self, objeto):
    if (self.size != self.defaultSize):
      self.elements[self.size] = objeto
      self.size = self.size+1
    else:
      self.extend()
      self.elements[self.size]
      self.size = self.size+1

  def addInIndex(self, index, objeto):
    if ((index < self.size) and (index >= 0)):
      if (self.size != self.defaultSize):
        for j in range(self.size, index-1, -1):
          self.elements[j] = self.elements[j-1]
        self.elements[index] = objeto
        self.size = self.size+1
      else:
        self.extend()
        for i in range(self.size, index-1, -1):
          self.elements[i] = self.elements[i-1]
        self.elements[index] = objeto
        self.size = self.size+1
    elif (index >= self.size):
      index = self.size
      if (self.size != self.defaultSize):
        for j in range(self.size, index-1, -1):
          self.elements[j] = self.elements[j-1]
        self.elements[index] = objeto
        self.size = self.size+1
      else:
        self.extend()
        for i in range(self.size+1, index-1, -1):
          self.elements[i] = self.elements[i-1]
        self.elements[index] = objeto
        self.size = self.size+1
    else:
      raise Exception("Index out of bounds")

  def extend(self):
    self.defaultSize = self.defaultSize*2
    elements2 = numpy.empty(self.defaultSize, dtype=object)
    for i in range(0, self.size):
      elements2[i] = self.elements[i]
    self.elements = elements2

  def remove(self, index):
    if ((index < self.size) and (index >= 0)):
      for i in range(index, self.size-1):
          self.elements[i] = self.elements[i+1]
      self.size = self.size-1
    else:
      raise Exception("Index out of bounds")

arr = ArrayList()
arr.add(1)
arr.add(2)
arr.add(3)
arr.add(4)
arr.add(5)
arr.add(6)
arr.add(7)
arr.add(8)
arr.add(9)
arr.add(10)
arr.remove(1)
arr.remove(3)
arr.remove(5)
arr.addInIndex(1, 10)
arr.addInIndex(3, 10)
arr.addInIndex(4, 8)
print(arr.get(0))
print(arr.get(1))
print(arr.get(2))
print(arr.get(3))
print(arr.get(4))
print(arr.get(5))
print(arr.get(6))
print(arr.get(7))
print(arr.get(8))
print(arr.get(9))
