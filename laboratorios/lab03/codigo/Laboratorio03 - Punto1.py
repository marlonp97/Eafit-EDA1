# Miguel Angel Sarmiento Aguiar
# Marlon Perez Rios

import pandas as pd

urlST0242 = 'https://raw.githubusercontent.com/mauriciotoro/ST0245-Eafit/master/laboratorios/lab03/datasets/NOTAS%20ST0242.csv'
urlST0245 = 'https://raw.githubusercontent.com/mauriciotoro/ST0245-Eafit/master/laboratorios/lab03/datasets/NOTAS%20ST0245.csv'
urlST0247 = 'https://raw.githubusercontent.com/mauriciotoro/ST0245-Eafit/master/laboratorios/lab03/datasets/NOTAS%20ST0247.csv'

STO242 = pd.read_csv(urlST0242)
STO245 = pd.read_csv(urlST0245)
STO247 = pd.read_csv(urlST0247)

Datos = []

def LlenarLista(Materia):
  global Datos
  Estudiante = []
  Estudiante.append(Materia.iat[0, 0])
  Estudiante.append(Materia.iat[0, 2])
  Estudiante.append(Materia.iat[0, 3])
  Estudiante.append(Materia.iat[0, 13])
  Datos.append(Estudiante)
  filMateria = Materia.shape[0]
  for k in range(1, filMateria):
    if ((Materia.iat[k, 0]) != (Materia.iat[k-1, 0])):
      Estudiante = []
      Estudiante.append(Materia.iat[k, 0])
      Estudiante.append(Materia.iat[k, 2])
      Estudiante.append(Materia.iat[k, 3])
      Estudiante.append(Materia.iat[k, 13])
      Datos.append(Estudiante)

LlenarLista(STO242)
LlenarLista(STO245)
LlenarLista(STO247)

def Consulta1(Curso, Semestre):
  global Datos
  DatosConsulta1 = []
  for i in range(len(Datos)):
    Temp = Datos[i]
    if ((Temp[1] == Curso) and (Temp[2] == Semestre)):
        EstudianteConsulta1 = []
        EstudianteConsulta1.append(Temp[0])
        EstudianteConsulta1.append(Temp[3])
        DatosConsulta1.append(EstudianteConsulta1)
  print(DatosConsulta1)

def Consulta2(Estudiante, Semestre):
  global Datos
  DatosConsulta2 = []
  for j in range(len(Datos)):
    Temp = Datos[j]
    if ((Temp[0] == Estudiante) and (Temp[2] == Semestre)):
        EstudianteConsulta2 = []
        EstudianteConsulta2.append(Temp[1])
        EstudianteConsulta2.append(Temp[3])
        DatosConsulta2.append(EstudianteConsulta2)
  print(DatosConsulta2)
