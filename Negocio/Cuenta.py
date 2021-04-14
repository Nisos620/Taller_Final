class Cuenta:
    def __init__(self, id, monto_inicial, minimo, porcentaje, saldo):
        self.id = id
        self.monto_inicial= monto_inicial
        self.minimo=minimo
        self.porcentaje=porcentaje
        self.saldo=saldo

    def get_id(self):
        return self.id

    def getMontoInicial(self):
        return self.monto_inicial

    def getMinimo(self):
        return self.minimo()

    def getPorcentaje(self):
        return self.porcentaje

    def getSaldo(self):
        return self.saldo

    def set_id(self, id):
        self.id = id

    def setMontoInicial(self,monto):
        self.monto_inicial=monto

    def setMinimo(self,minimo):
        self.minimo=minimo

    def setPorcentaje(self,porcentaje):
        self.porcentaje=porcentaje

    def mostrar_datos(self):
        print("Id: ", self.id, ",Monto inicial cuenta: ", self.monto_inicial, ",Minimo: "
              , self.minimo, ",Porcentaje: ", self.porcentaje,",Saldo:", self.saldo)