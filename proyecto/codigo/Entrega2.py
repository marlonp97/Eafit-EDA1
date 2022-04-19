# Entrega 2

# Miguel Angel Sarmiento Aguiar
# Marlon Perez Rios

def Crear_Estructura_Datos(Direccion_csv):
  Archivo_csv = open(Direccion_csv, "rt")           # C1
  Texto = Archivo_csv.read()                        # C2
  Texto = Texto[:len(Texto)-1]                      # C3
  Datos = Texto.split("\n")                         # C4*n
  for Fila, i in zip(Datos, range(len(Datos))):     # C5*n
    Datos[i] = Fila.split(";")                      # C6*n*m
  Archivo_csv.close()                               # C7
  return Datos                                      # C8

# n = Número de filas
# m = Número de columnas
