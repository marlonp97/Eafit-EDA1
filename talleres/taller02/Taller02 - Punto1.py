# Punto 1

# Camilo Villa Tamayo
# Miguel Angel Sarmiento Aguiar
# Marlon Perez Rios

def gcdEuclidiana(p,q):
    
    if q == 0:
        return p
    
    return gcdEuclidiana(q, p%q)

p = int(input("Ingrese el primer número: "))
q = int(input("Ingrese el segundo número: "))
 
print("El MCD entre ", p, " y ", q, " es ", gcdEuclidiana(p,q))
