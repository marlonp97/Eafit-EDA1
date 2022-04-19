# Punto 1

# Miguel Angel Sarmiento Aguiar
# Marlon Perez Rios

class HashTable():

  def __init__(self):
    self.tabla = [None]*10

  def funcion_hash(self, k):
    key = 0
    for i in range(len(k)):
      key += ord(k[i])*10^i
    return key%10

  def get(self, k):
    print(self.tabla[self.funcion_hash(k)])

  def put(self, k, v):
    self.tabla[self.funcion_hash(k)] = v

H = HashTable()
H.put("Marlon", 3107353554)
H.put("Miguel", 3108906839)
H.get("Marlon")
H.get("Miguel")
