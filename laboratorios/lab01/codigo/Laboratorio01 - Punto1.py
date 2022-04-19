# Camilo Villa Tamayo
# Miguel Angel Sarmiento Aguiar
# Marlon Perez Rios

# Punto 1.1

def lcsDNA(string1, string2):
  return lcsDNAaux(string1, string2, len(string1), len(string2))

def lcsDNAaux(string1, string2, m, n):
  if (m == 0 or n == 0):
    return 0
  if (string1[m-1] == string2[n-1]):
    return 1 + lcsDNAaux(string1[:m-1], string2[:n-1] , m-1, n-1)
    
  return max(lcsDNAaux(string1, string2[:n-1], m, n-1), lcsDNAaux(string1[:m-1], string2, m-1, n))
     
print(lcsDNA("AGGTAB", "GXTXAYB"))

# Punto 1.2

def formas(n):
  if (n <= 2):
    return n
  else:
    return formas(n-1) + formas (n-2)

formas(4)
