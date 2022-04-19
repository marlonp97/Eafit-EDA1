# Miguel Angel Sarmiento Aguiar
# Marlon Perez Rios

def TecladoRoto(Entrada):
  Lista = []
  Start = True
  Index = 0
  Texto = ''
  for i in range(len(Entrada)):
    if (Entrada[i] == '['):
      Start = True
      Index = 0
    elif (Entrada[i] == ']'):
      Start = False
    elif ((Entrada[i] != '[') and (Entrada[i] != ']')):
      if (Start):
        Lista.insert(Index, Entrada[i])
        Index = Index+1
      else:
        Lista.append(Entrada[i])
  for j in range(len(Lista)):
    Texto = Texto + Lista[j]
  print(Texto)
