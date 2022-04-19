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

b = BinaryTree()
b.insertar(3)
b.insertar(4)
b.insertar(5)
print(b.buscar(4))
