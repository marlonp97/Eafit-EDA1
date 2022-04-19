# Miguel Angel Sarmiento Aguiar
# Marlon Perez Rios

class Nodo:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data
    
class BinaryTree:
  def __init__(self):
    self.root = None

  def insertar(self, n):
    if self.root == None:
      self.root = Nodo(n)
    else:
      return self.insertar_aux(self.root, n)
      
  def insertar_aux(self, node, n):
    if n > node.data:
      if node.right == None:
        node.right = Nodo(n)
      else:
        return self.insertar_aux(node.right, n)
    else:
      if node.left == None:
        node.left = Nodo(n)
      else:
        return self.insertar_aux(node.left, n)

  def buscar(self, n):
    return self.buscar_aux(self.root, n)
    
  def buscar_aux(self, node, n):
    if node == None:
      return False
    if node.data == n:
      return True
    if n > node.data:
      return self.buscar_aux(node.right, n)
    else:
      return self.buscar_aux(node.left, n)

  def preorden(self, node):
    if node != None:                    # C1
      print(node.data)                  # C2
      self.preorden(node.left)          # C3*(n/2)
      self.preorden(node.right)         # C4*(n/2)

  def posorden(self, node):
    if node != None:                    # C1
      self.posorden(node.left)          # C2*(n/2)
      self.posorden(node.right)         # C3*(n/2)
      print(node.data)                  # C4

  def inorden(self, node):
    if node != None:                    # C1
      self.inorden(node.left)           # C2*(n/2)
      print(node.data)                  # C3
      self.inorden(node.right)          # C4*(n/2)

b = BinaryTree()
b.insertar(50)
b.insertar(30)
b.insertar(98)
b.insertar(24)
b.insertar(45)
b.insertar(52)
b.insertar(5)
b.insertar(28)
b.insertar(60)

print("Pre-Orden:")
b.preorden(b.root)
print("Pos-Orden:")
b.posorden(b.root)
print("In-Orden:")
b.inorden(b.root)
