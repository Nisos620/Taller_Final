class Banco:
    def __init__(self, sucursal, direccion):
        self.sucursal = sucursal
        self.direccion = direccion
        self.lista_empleados=list()

    def getSucursal(self):
        return self.sucursal

    def getDireccion(self):
        return self.direccion
    def getEmpleados(self):
        return self.lista_empleados

    def setSucursal(self,sucursal):
        self.sucursal=sucursal

    def setDireccion(self,direccion):
        self.direccion=direccion

    def mostrasDatos(self):
        print('Sucursal: ',self.sucursal,' direccion: ',self.direccion, 'cantidad de empleados')

    def agregarEmpleado(self, empleado):
        self.lista_empleados.append(empleado)

    def mostrarEmpleados(self):
        for emplados in self.lista_empleados():
            emplados.mostrasDatos()






