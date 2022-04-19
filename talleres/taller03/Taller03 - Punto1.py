# Punto 1

# Camilo Villa Tamayo
# Miguel Angel Sarmiento Aguiar
# Marlon Perez Rios

def hanoi1(topN):
  hanoi(topN, "Torre 1", "Torre 2", "Torre 3")

def hanoi(topN, a, b, c):
  if topN == 1:
    print("Disco 1 desde " + a + " hasta " + c)
  else:
    hanoi(topN - 1, a, c, b)
    print("Disco " + str(topN) + " desde " + a + " hasta " + c)
    hanoi(topN - 1, b, a, c)

hanoi1(3)
