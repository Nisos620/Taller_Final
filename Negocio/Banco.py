class Banco:
    def __init__(self, sucursal, direccion):
        self.sucursal = sucursal
        self.direccion = direccion

    def getSucursal(self):
        return self.sucursal

    def getDireccion(self):
        return self.direccion

    def setSucursal(self,sucursal):
        self.sucursal=sucursal

    def setDireccion(self,direccion):
        self.direccion=direccion
