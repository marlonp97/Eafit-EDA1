# Miguel Angel Sarmiento Aguiar
# Marlon Perez Rios

import numpy as np

def Crear_Lista_Instrucciones(Entrada):
  ListaInstrucciones = []
  Cont = 0
  while Cont < len(Entrada):
    if (Entrada[Cont] != "0"):
      if ((" " not in Entrada[Cont]) and (" " not in Entrada[Cont+1])):
        if Cont > 0:
          ListaInstrucciones.append(Lista)
        Lista = [Entrada[Cont]]
        Cont += 2      
      elif (" " in Entrada[Cont]):
        Lista.append(Entrada[Cont])
        Cont += 1
    else:
      ListaInstrucciones.append(Lista)
      Cont += 1
  return ListaInstrucciones

def Crear_Mapas(ListaInstrucciones):
  Mapas = [[] for _ in range(len(ListaInstrucciones))]
  for i in range(len(ListaInstrucciones)):
    Mapas[i] = np.zeros((int(ListaInstrucciones[i][0]), int(ListaInstrucciones[i][0])))
    for j in range(1, len(ListaInstrucciones[i])):
      Mapas[i][int(ListaInstrucciones[i][j].split(" ")[0])][int(ListaInstrucciones[i][j].split(" ")[1])] = 1
      Mapas[i][int(ListaInstrucciones[i][j].split(" ")[1])][int(ListaInstrucciones[i][j].split(" ")[0])] = 1
  return Mapas

# Título: Check whether a given graph is Bipartite or not
# Autor: Divyanshu Mehta
# Tomado de: https://www.geeksforgeeks.org/bipartite-graph/

class Graph():
  def __init__(self, V):
    self.V = V
    self.graph = [[0 for column in range(V)] \
                  for row in range(V)]

  def isBipartite(self, src):
    colorArr = [-1] * self.V
    colorArr[src] = 1
    queue = []
    queue.append(src)
    while queue:
      u = queue.pop()
      if self.graph[u][u] == 1:
        return False
      for v in range(self.V):
        if self.graph[u][v] == 1 and colorArr[v] == -1:
          colorArr[v] = 1 - colorArr[u]
          queue.append(v)
        elif self.graph[u][v] == 1 and colorArr[v] == colorArr[u]:
          return False
    return True

Entrada = ["3","3","0 1","1 2","2 0","3","2","0 1","1 2","9","8","0 1","0 2","0 3","0 4","0 5","0 6","0 7","0 8","0"]
ListaInstrucciones = Crear_Lista_Instrucciones(Entrada)
Mapas = Crear_Mapas(ListaInstrucciones)
for i in range(len(Mapas)):
  Grafo = Graph(len(Mapas[i]))
  Grafo.graph = Mapas[i]
  print ("BICOLORABLE" if Grafo.isBipartite(0) else "NOT BICOLORABLE")
