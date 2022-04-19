# Miguel Angel Sarmiento Aguiar
# Marlon Perez Rios

# Punto 1.1

import numpy as np

class GraphAm:

    def __init__(self, size):
      self.matriz = np.zeros((size, size))
      self.numVertices = size

    def addArc(self, source, destination, weight):
      self.matriz[source][destination] = weight

    def getWeight(self, source, destination):
      return self.matriz[source][destination]

    def getSuccessors(self, vertex):
      lista = []
      for i in range(self.numVertices):
        if (self.matriz[vertex][i] != 0):
          lista.append(i)
      return lista

GrafoAm = GraphAm(3)
GrafoAm.addArc(0, 1, 2)
GrafoAm.addArc(0, 2, 3)
print(GrafoAm.getWeight(0, 1))
print(GrafoAm.getWeight(0, 2))
print(GrafoAm.getSuccessors(0))

# Punto 1.2
  
class GraphAL:

    def __init__(self, size):
      self.lista = [[] for _ in range(3)]

    def addArc(self, source, destination, weight):
      self.lista[source].append((destination, weight))

    def getWeight(self, source, destination):
      peso = 0
      for i in range(len(self.lista[source])):
        if (self.lista[source][i][0] == destination):
          peso = self.lista[source][i][1]
      return peso

    def getSuccessors(self, vertex):
      listaS = []
      for i in range(len(self.lista[vertex])):
        listaS.append(self.lista[vertex][i][0])
      return listaS

GrafoAL = GraphAL(3)
GrafoAL.addArc(0, 1, 2)
GrafoAL.addArc(0, 2, 3)
print(GrafoAL.getWeight(0, 1))
print(GrafoAL.getWeight(0, 2))
print(GrafoAL.getSuccessors(0))
