# Miguel Angel Sarmiento Aguiar
# Marlon Perez Rios

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

# Punto 1

def hay_Camino_DFS(Grafo_g, Vertice_i, Vertice_j):
  Visitados = [0]*Grafo_g.numVertices
  return hay_Camino_DFSAux(Grafo_g, Vertice_i, Vertice_j, Visitados)

def hay_Camino_DFSAux(Grafo_g, Vertice_i, Vertice_j, Visitados):
  Visitados[Vertice_i] = 1
  if (Vertice_i == Vertice_j):
    return True
  else:
    for Hijo in Grafo_g.getSuccessors(Vertice_i):
      if (not Visitados[Hijo] == 1):
        if (hay_Camino_DFSAux(Grafo_g, Hijo, Vertice_j, Visitados)):
          return True
    return False

# Punto 2

def hay_Camino_BFS(Grafo_g, Vertice_i, Vertice_j):
  Visitados = [0]*Grafo_g.numVertices
  Cola = []
  Cola.append(Vertice_i)
  Visitados[Vertice_i] = 1
  if (Vertice_i == Vertice_j):
    return True
  else:
    while Cola:
      n = Cola.pop(0)
      if (n == Vertice_j):
        return True
      for Hijo in Grafo_g.getSuccessors(n):
        if (Visitados[Hijo] == 0):
          Cola.append(Hijo)
          Visitados[Hijo] = 1
    return False

GrafoAm = GraphAm(4)
GrafoAm.addArc(0, 1, 2)
GrafoAm.addArc(1, 2, 3)
GrafoAm.addArc(2, 0, 4)
GrafoAm.addArc(3, 3, 2)
print(hay_Camino_DFS(GrafoAm, 0, 2))
print(hay_Camino_DFS(GrafoAm, 1, 3))
print(hay_Camino_BFS(GrafoAm, 0, 2))
print(hay_Camino_BFS(GrafoAm, 1, 3))
