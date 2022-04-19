# Punto 2

# Camilo Villa Tamayo
# Miguel Angel Sarmiento Aguiar
# Marlon Perez Rios

def permutations1(stri):
  permutations("", stri)



def permutations(base, stri):
  n = len(stri)
  if n == 0:
    print(base)
  else:
    for i in range(n):
      permutations(base + stri[i] , stri[0:i] + stri[i+1:n])

permutations1("abc")
