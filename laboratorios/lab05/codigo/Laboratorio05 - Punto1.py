# Miguel Angel Sarmiento Aguiar
# Marlon Perez Rios

import pandas as pd

url_Vertices = "https://raw.githubusercontent.com/mauriciotoro/ST0245-Eafit/master/laboratorios/lab05/codigo_estudiante/codigo/Python/Vertices.csv"
url_Arcos = "https://raw.githubusercontent.com/mauriciotoro/ST0245-Eafit/master/laboratorios/lab05/codigo_estudiante/codigo/Python/Arcos.csv"

Vertices = pd.read_csv(url_Vertices)
Arcos = pd.read_csv(url_Arcos)
Vertices.columns = ['ID', 'Coordenada X', 'Coordenada Y', 'Nombre']
Arcos.columns = ['ID', 'ID1', 'Distancia', 'Nombre']

dicc_Vertices = {}
for i in range(len(Vertices)):
  dicc_Vertices[(Vertices.iloc[i]['ID'])] = Vertices.iloc[i]['Nombre']

dicc_Arcos = {}
for i in range(len(Arcos)):
  dicc_Arcos[(Arcos.iloc[i]['ID'], Arcos.iloc[i]['ID1'])] = Arcos.iloc[i]['Distancia']

print("La estructura de datos de los vértices es:")
print(dicc_Vertices)

print("La estructura de datos de los arcos es:")
print(dicc_Arcos)
