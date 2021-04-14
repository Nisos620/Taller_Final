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
        cuenta_id = self.generar_id()
        self.lista_cuentas.append(Cuenta(cuenta_id, monto_inicial, minimo, porcentaje, saldo))

    def eliminar_cuenta(self, id_cuenta):
        self.lista_cuentas.pop(id_cuenta - 1)

    def generar_id(self):
        nuevo_id = len(self.lista_cuentas) + 1

        return nuevo_id

    def mostrar_cuenta(self):
        for i in range(len(self.lista_cuentas)):
            print("Numero de cuenta: ", i + 1)
            print(self.lista_cuentas[i].mostrar_datos())
        return len(self.lista_cuentas)