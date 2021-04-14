from Negocio.Cuenta import Cuenta


class Cliente:

    def __init__(self, nombre, usuario, identificacion):
        self.nombre = nombre
        self.usuario = usuario
        self.identificacion = identificacion
        self.lista_cuentas = list()

    def getNombre(self):
        return self.nombre

    def getUsuario(self):
        return self.usuario

    def getIdentificacion(self):
        return self.identificacion

    def get_lista_cuentas(self):
        return self.lista_cuentas

    def setnombre(self, nombre):
        self.nombre = nombre

    def setUsuario(self, usuario):
        self.usuario = usuario

    def setIdentificacion(self, identificacion):
        self.identificacion = identificacion

    def añadir_cuenta(self, monto_inicial, minimo, porcentaje, saldo):
        cuenta_id = self.generar_id(self)
        self.lista_cuentas.append(cuenta_id, monto_inicial, minimo, porcentaje, saldo)

    def generar_id(self):
        nuevo_id = len(self.lista_cuentas) + 1

        return nuevo_id
