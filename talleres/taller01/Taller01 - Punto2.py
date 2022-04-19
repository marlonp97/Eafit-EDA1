# Fecha

# Camilo Villa Tamayo
# Miguel Angel Sarmiento Aguiar
# Marlon Perez Rios

class Fecha:

    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año

    def get_dia(self):
        return self.dia

    def get_mes(self):
    		return self.mes
    
    def get_año(self):
    		return self.año
    
date1 = Fecha(2, 4, 2017)
date2 = Fecha(2, 4, 2017)

print("Fecha 1:", str(date1.get_dia()) + "/" + str(date1.get_mes()) + "/" + str(date1.get_año()))
print("Fecha 2:", str(date2.get_dia()) + "/" + str(date2.get_mes()) + "/" + str(date2.get_año()))

if date1.get_año() == date2.get_año():
  
  if date1.get_mes() == date2.get_mes():
    
    if date1.get_dia() == date2.get_dia():

      print("La fecha " + str(date1.get_dia()) + " de " + str(date1.get_mes()) + " de " + str(date1.get_año()) + " es igual a " + str(date2.get_dia()) + " de " + str(date2.get_mes()) + " de " + str(date2.get_año()))

    elif date1.get_dia() < date2.get_dia():

      print("La fecha " + str(date1.get_dia()) + " de " + str(date1.get_mes()) + " de " + str(date1.get_año()) + " está antes de " + str(date2.get_dia()) + " de " + str(date2.get_mes()) + " de " + str(date2.get_año()))

    else:

      print("La fecha " + str(date1.get_dia()) + " de " + str(date1.get_mes()) + " de " + str(date1.get_año()) + " está después de " + str(date2.get_dia()) + " de " + str(date2.get_mes()) + " de " + str(date2.get_año()))
  
  elif date1.get_mes() < date2.get_mes():

    print("La fecha " + str(date1.get_dia()) + " de " + str(date1.get_mes()) + " de " + str(date1.get_año()) + " está antes de " + str(date2.get_dia()) + " de " + str(date2.get_mes()) + " de " + str(date2.get_año()))

  else:

    print("La fecha " + str(date1.get_dia()) + " de " + str(date1.get_mes()) + " de " + str(date1.get_año()) + " está después de " + str(date2.get_dia()) + " de " + str(date2.get_mes()) + " de " + str(date2.get_año()))

elif date1.get_año() < date2.get_año():

  print("La fecha " + str(date1.get_dia()) + " de " + str(date1.get_mes()) + " de " + str(date1.get_año()) + " está antes de " + str(date2.get_dia()) + " de " + str(date2.get_mes()) + " de " + str(date2.get_año()))

else:

  print("La fecha " + str(date1.get_dia()) + " de " + str(date1.get_mes()) + " de " + str(date1.get_año()) + " está despues de " + str(date2.get_dia()) + " de " + str(date2.get_mes()) + " de " + str(date2.get_año()))
