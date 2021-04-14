from Negocio.Cuenta import Cuenta


class Casa_Inversionista:

    def __init__(self, nombre, clave, porcentajes_retorno, montos, plazos, nivel_riesgo):
        self.nombre = nombre
        self.clave = clave
        self.porcentajes = porcentajes_retorno
        self.montos = montos
        self.plazos = plazos
        self.nivel = nivel_riesgo
        self.lista_cuentas = list()

    def getNombre(self):
        return self.nombre

    def getClave(self):
        return self.clave

    def getPorcentajes(self):
        return self.porcentajes

    def getMontos(self):
        return self.montos

    def getPlazos(self):
        return self.plazos

    def getNivel(self):
        return self.nivel

    def setNombre(self, nombre):
        self.nombre = nombre

    def setClave(self, clave):
        self.clave = clave

    def setPorcentajes(self, porcentajes):
        self.porcentajes = porcentajes

    def setMontos(self, montos):
        self.montos = montos

    def setPlazos(self, plazos):
        self.plazos = plazos

    def setNivel(self, plazo):
        self.plazos = plazo

    def mostrarDatos(self):
        print("Nombre: ", self.nombre, ", Clave: ", self.clave, ", Porcentaje de retorno: "
              , self.porcentajes, ", Monto: ", self.montos, ", Plazo: ", self.plazos, ", Nivel de riesgo: ", self.nivel)

    def agregarCuenta(self):
        varMontoInicial = int(input('Ingresa el valor del monto inicial: '))
        varMinimo = int(input('Ingresa el valor del minimo: '))
        varPorcentaje = float(input('Ingresa el porcentaje: '))
        varSaldo = int(input('Ingresa el saldo: '))

        self.lista_cuentas.append(Cuenta(varMontoInicial, varMinimo, varPorcentaje, varSaldo))

    def eliminarCuenta(self, parPosicion):
        self.lista_cuentas.pop(parPosicion)

    def mostrarDatosCuenta(self):
        for i in range(len(self.lista_cuentas)):
            print(i)
            print(self.lista_cuentas[i].mostrarDatos())
