# Punto 3

# Camilo Villa Tamayo
# Miguel Angel Sarmiento Aguiar
# Marlon Perez Rios

def subconjuntos(s):
  subconjuntosBase("", s)
  
def subconjuntosBase(base, t):
  if len(t) == 0:
    print(base)
  else:
    subconjuntosBase(base + t[0], t[1:])
    subconjuntosBase(base, t[1:])

subconjuntos("Santi")
