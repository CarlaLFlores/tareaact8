class Cuenta:
  def __init__(self,titular,saldo=0):
    self.titular=titular
    self.saldo=saldo
  def datos_cuenta(self, titular,saldo):
    print (f"La cuenta pertenece a",{titular}, "su saldo es",{saldo})
  def ingresar (self, num_1):
    self.num_1=num_1
    print (f"Su saldo es:", self.saldo+num_1)
  def extraer (self, num_2):
    self.num_2=num_2
    if self.saldo> self.num_2:
      print (f"Su saldo es:",self.saldo-num_2)
    elif self.saldo< self.num_2:
      print(f"Su saldo es:",self.saldo-num_2)
cuenta1= Cuenta ("Carla Flores", 50000)
cuenta1.datos_cuenta ("Carla Flores", 50000)
cuenta1.ingresar(-5000)
cuenta1.extraer(55000)