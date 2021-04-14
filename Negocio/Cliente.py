from Negocio.Cuenta import Cuenta


class Cliente:

    def __init__(self,nombre,usuario,identificacion):
        self.nombre= nombre
        self.usuario= usuario
        self.identificacion= identificacion
        self.lista_cuentas = list()

    def getNombre(self):
        return self.nombre

    def getUsuario(self):
        return self.usuario

    def getIdentificacion(self):
        return self.identificacion

    def get_lista_cuentas(self):
        return self.lista_cuentas

    def setnombre(self,nombre):
        self.nombre=nombre

    def setUsuario(self, usuario):
        self.usuario=usuario

    def setIdentificacion(self,identificacion):
        self.identificacion=identificacion

    def añadir_cuenta(self, id, monto_inicial, minimo, porcentaje, saldo):
        existe_cuenta = -1
        index = 0
        for i in self.lista_cuentas:
            if i.get_id() == id:
                existe_cuenta = index
                index += 1

        if existe_cuenta > -1:
            print('El id ya está registrado')
        else:
            self.lista_cuentas.append(Cuenta(id, monto_inicial, minimo, porcentaje, saldo))
            print('Se agregó la cuenta')
