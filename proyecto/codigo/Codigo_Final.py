# Proyecto EDA1

# Miguel Angel Sarmiento Aguiar
# Marlon Perez Rios

# Datos de entrenamiento

Train_0 = "/content/drive/My Drive/Datasets/0_train_balanced_15000.csv"
Train_1 = "/content/drive/My Drive/Datasets/1_train_balanced_45000.csv"
Train_2 = "/content/drive/My Drive/Datasets/2_train_balanced_75000.csv"
Train_3 = "/content/drive/My Drive/Datasets/3_train_balanced_105000.csv"
Train_4 = "/content/drive/My Drive/Datasets/4_train_balanced_135000.csv"
Train_5 = "/content/drive/My Drive/Datasets/5_train_balanced_57765.csv"

Train = [Train_0, Train_1, Train_2, Train_3, Train_4, Train_5]

# Datos de prueba

Test_0 = "/content/drive/My Drive/Datasets/0_test_balanced_5000.csv"
Test_1 = "/content/drive/My Drive/Datasets/1_test_balanced_15000.csv"
Test_2 = "/content/drive/My Drive/Datasets/2_test_balanced_25000.csv"
Test_3 = "/content/drive/My Drive/Datasets/3_test_balanced_35000.csv"
Test_4 = "/content/drive/My Drive/Datasets/4_test_balanced_45000.csv"
Test_5 = "/content/drive/My Drive/Datasets/5_test_balanced_19255.csv"

Test = [Test_0, Test_1, Test_2, Test_3, Test_4, Test_5]

# Crear estructura de datos

def Crear_Estructura_Datos(Direccion_csv):
  Archivo_csv = open(Direccion_csv, "rt", encoding="utf-8")
  Texto = Archivo_csv.read()
  Texto = Texto[:len(Texto)-1]
  Datos = Texto.split("\n")
  for Fila, i in zip(Datos, range(len(Datos))):
    Datos[i] = Fila.split(";")
  Archivo_csv.close()
  return Datos

# Dividir matriz en dos

def Dividir_Matriz_En_Dos(Matriz, Pos_Variable, Valor):
  Pareja_Matrices = ([i for i in Matriz if i[Pos_Variable] == Valor], [j for j in Matriz if j[Pos_Variable] != Valor])
  return Pareja_Matrices

# Calcular diferentes valores de una variable

def Calcular_Valores_Variable(Matriz, Pos_Variable):
  Columna = [i[Pos_Variable] for i in Matriz]
  Valores = list(set(Columna))
  return Valores

# Calcular posición de la mejor variable y valor

def Calcular_Mejor_Variable(Matriz):
  Impureza_Menor = 1
  Valor_Mejor = ''
  Posicion_Valor_Mejor = -1
  Filas = len(Matriz)
  Matriz_Total_Tienen_Exito = ['' for i in Matriz if i[-1] == '1']
  Total_Tienen_Exito = len(Matriz_Total_Tienen_Exito)
  Total_No_Tienen_Exito = Filas - Total_Tienen_Exito
  for Pos_Variable in range(len(Matriz[0])-1):
    Valores = Calcular_Valores_Variable(Matriz, Pos_Variable)
    if (len(Valores) > 1):
      Listas = [[0, 0] for j in range(len(Valores))]
      Diccionario = dict(zip(Valores, Listas))
      for Fila in range(Filas):
        if (Matriz[Fila][-1] == '1'):
          Diccionario[Matriz[Fila][Pos_Variable]][0] += 1
        else:
          Diccionario[Matriz[Fila][Pos_Variable]][1] += 1
      for Valor in Diccionario:
        Elementos_Variable_Igual = Diccionario[Valor][0] + Diccionario[Valor][1]
        Impureza_Variable_Igual = 1 - (Diccionario[Valor][0]/Elementos_Variable_Igual)**2 - (Diccionario[Valor][1]/Elementos_Variable_Igual)**2
        Tienen_Exito_Variable_Diferente = Total_Tienen_Exito - Diccionario[Valor][0]
        No_Tienen_Exito_Variable_Diferente = Total_No_Tienen_Exito - Diccionario[Valor][1]
        Elementos_Variable_Diferente = Tienen_Exito_Variable_Diferente + No_Tienen_Exito_Variable_Diferente
        Impureza_Variable_Diferente = 1 - (Tienen_Exito_Variable_Diferente/Elementos_Variable_Diferente)**2 - (No_Tienen_Exito_Variable_Diferente/Elementos_Variable_Diferente)**2
        Impureza_Ponderada = (Impureza_Variable_Igual*Elementos_Variable_Igual + Impureza_Variable_Diferente*Elementos_Variable_Diferente) / Filas
        if (Impureza_Ponderada < Impureza_Menor):
          Impureza_Menor = Impureza_Ponderada
          Valor_Mejor = Valor
          Posicion_Valor_Mejor = Pos_Variable
  Pareja_Valor_Mejor = (Posicion_Valor_Mejor, Valor_Mejor)
  return Pareja_Valor_Mejor

# Crear árbol de búsqueda

class Nodo:
  def __init__(self, Matriz, Nivel_Maximo, Nivel = 0):
    if ((Nivel + 1) == Nivel_Maximo):
      self.matriz = Matriz
      self.prob_exito = Calcular_Probabilidad_Exito(Matriz)
      self.si = None
      self.no = None
      self.variable, self.valor = Calcular_Mejor_Variable(self.matriz)
      return None
    else:
      self.matriz = Matriz
      self.variable, self.valor = Calcular_Mejor_Variable(self.matriz)
      Matriz_Si, Matriz_No = Dividir_Matriz_En_Dos(self.matriz, self.variable, self.valor)
      self.si = Nodo(Matriz_Si, Nivel_Maximo, Nivel + 1)
      self.no = Nodo(Matriz_No, Nivel_Maximo, Nivel + 1)

class Arbol_Binario:
  def __init__(self, Matriz, Nivel_Maximo):
    self.raiz = Nodo(Matriz, Nivel_Maximo)

  def dibujar(self, Titulos):
    return 'digraph G {\n' + self.dibujar_Aux(Titulos, self.raiz) + '}'

  def dibujar_Aux(self, Titulos, Node):
    if ((Node.si == None) and (Node.no == None)):
      return ''
    else:
      return ' \"' + str(Titulos[Node.variable]) + ' == ' + str(Node.valor) + '" -> "' + str(Titulos[Node.no.variable]) + ' == ' + str(Node.no.valor) + '"\n' + ' \"' + str(Titulos[Node.variable]) + ' == ' + str(Node.valor) + '" -> "' + str(Titulos[Node.si.variable]) + ' == ' + str(Node.si.valor) + '"\n' + self.dibujar_Aux(Titulos, Node.no) + self.dibujar_Aux(Titulos, Node.si)

# Calcular probabilidad de éxito

def Calcular_Probabilidad_Exito(Matriz):
  Filas = len(Matriz)
  Matriz_Tienen_Exito = ['' for i in Matriz if i[-1] == '1']
  Tienen_Exito = len(Matriz_Tienen_Exito)
  Probabilidad_Exito = Tienen_Exito / Filas
  return Probabilidad_Exito

# Calcular pronóstico de éxito

def Calcular_Pronostico_Exito(Fila, Arbol):
  if ((Arbol.si == None) and (Arbol.no == None)):
    return Arbol.prob_exito
  else:
    if (Fila[Arbol.variable] == Arbol.valor):
      return Calcular_Pronostico_Exito(Fila, Arbol.si)
    else:
      return Calcular_Pronostico_Exito(Fila, Arbol.no)

# Calcular éxito colectivo:

def Calcular_Exito_Colectivo(Matriz, Arbol):
  Tienen_Exito_Real = 0
  Tienen_Exito_Pronostico = 0
  for Fila in Matriz:
    if (Fila[-1] == '1'):
      Tienen_Exito_Real += 1
    Pronostico = Calcular_Pronostico_Exito(Fila, Arbol.raiz)
    if (Pronostico >= 0.5):
      Tienen_Exito_Pronostico += 1
  Error = (abs(Tienen_Exito_Pronostico - Tienen_Exito_Real) / Tienen_Exito_Real)
  Exito = (Tienen_Exito_Real, Tienen_Exito_Pronostico, Error)
  return Exito

# Calcular éxito individual:

def Calcular_Exito_Individual(Matriz, Arbol):
  Probabilidad_Pronostico = Calcular_Pronostico_Exito(Matriz, Arbol.raiz)
  if (Probabilidad_Pronostico >= 0.5):
    Pronostico = 'Sí'
  else:
    Pronostico = 'No'
  Exito = (Pronostico, Probabilidad_Pronostico)
  return Exito

# Programa principal

def main(Train, Test, Nivel_Arbol, Fila):
  Estructura_Train = Crear_Estructura_Datos(Train)
  Estructura_Test = Crear_Estructura_Datos(Test)
  Estructura_Test = Estructura_Test[1:]
  Arbol = Arbol_Binario(Estructura_Train[1:], Nivel_Arbol)
  WebGraphviz = Arbol.dibujar(Estructura_Train[0])
  if (Fila == 'All'):
    Exito_Real, Exito_Pronostico, Error = Calcular_Exito_Colectivo(Estructura_Test, Arbol)
    print('Tipo de análisis: Colectivo\n\nTotal estudiantes: ' + str(len(Estructura_Test)) + '\n\nAlgoritmo:\nÉxito: ' + str(Exito_Pronostico) + '\nNo éxito: ' + str(len(Estructura_Test)-Exito_Pronostico) + '\n\nReal:\nÉxito: ' + str(Exito_Real) + '\nNo éxito: ' + str(len(Estructura_Test)-Exito_Real) + '\n\nError del algoritmo: ' + str(round(Error*100, 2)) + '%\n\nCódigo para graficar árbol en WebGraphviz:\n' + WebGraphviz)
  elif ((Fila >= 0) and (Fila < len(Estructura_Test))):
    Exito_Pronostico, Probabilidad_Pronostico = Calcular_Exito_Individual(Estructura_Test[Fila], Arbol)
    if (Estructura_Test[Fila][-1] == '1'):
      Exito_Real = 'Sí'
    else:
      Exito_Real = 'No'
    print('Tipo de análisis: Individual\n\nAlgoritmo:\nÉxito: ' + str(Exito_Pronostico) + '\nProbabilidad: ' + str(round(Probabilidad_Pronostico*100, 2)) + '%\n\nReal:\nÉxito: ' + str(Exito_Real) + '\n\nCódigo para graficar árbol en WebGraphviz:\n' + WebGraphviz)
  else:
    print('Índice de estudiante fuera de los límites')

main(Train[1], Test[1], 5, 'All')
