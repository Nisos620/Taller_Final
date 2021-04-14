from Negocio.Banco import Banco
from Negocio.Casa_Inversionista import Casa_Inversionista
from Negocio.Cliente import Cliente

lista_bancos = list()
lista_Casas_Inversionistas = list()
lista_cliente = list()
varOpcionMenuPrincipal = 0

def crearBanco():
    sucursal=input('Ingrese la sucursal del banco')
    direccion=input('Ingrese la direccion del banco')
    a= existSucursal(sucursal)
    if not a:
        lista_bancos.append(Banco(sucursal,direccion))
    else:
        print('ese banco ya existe ')

def existSucursal(sucursal):
    existe = False
    for bancos in lista_bancos:
        if (sucursal == bancos.getSucursal()):
            existe = True
    return existe

def EliminarBanco():
    sucursal = input('Ingrese la sucursal del banco')
    a = existSucursal(sucursal)
    if a:
        for bancos in lista_bancos:
            if sucursal==bancos.getSucursal():
                posicion = lista_bancos.index(bancos)
        lista_bancos.pop(posicion)
        print('banco eliminado')
    else:
        print('ese banco no  existe ')

def ModificarBanco():
    sucursal = input('Ingrese la sucrusal del banco')
    a = existSucursal(sucursal)
    if a:
        for bancos in lista_bancos:
            if sucursal==bancos.getSucursal():
                posicion = lista_bancos.index(bancos)
        sucursal = input('Ingrese nueva sucursal del banco')
        direccion= input('ingrese  nueva direccion del banco')
        lista_bancos[posicion].setSucursal(sucursal)
        lista_bancos[posicion].setDireccion(direccion)
    else:
        print('ese banco no  existe ')

def mostrasBanco():
    sucursal = input('Ingrese la sucrusal del banco')
    a = existSucursal(sucursal)
    if a:
        for bancos in lista_bancos:
            if sucursal == bancos.getSucursal():
                posicion = lista_bancos.index(bancos)
        lista_bancos[posicion].mostrasDatos()
    else:
        print('ese banco no  existe ')


def MenuPrincipal():
    print("\n*****************************")
    print("*******MENU PRINCIPAL********")
    print("*****************************")
    print("1. Gestion Banco")
    print("2. Gestion Cliente(s)")
    print("3. Gestion Casa Inversionista")
    print("4. Gestion Empleados")
    print("5. Gestion Cuenta")
    print("6. Salir")


def MenuGestionBanco():
    print("\n*****************************")
    print("********MENU GESTION BANCO*********")
    print("*****************************")
    print("1. Crear Banco")
    print("2. Eliminar Banco")
    print("3. Modificar Banco")
    print("4. Informacion del Banco")
    print("5. Atras")


def MenuGestionCliente():
    print("\n*****************************")
    print("********MENU GESTION CLIENTE*********")
    print("*****************************")
    print("1. Crear Cliente")
    print("2. Añadir cuenta a cliente")
    print("3. Eliminar cuenta a cliente")
    print("4. Mostrar Informacion cuenta")
    print("5. Atras")


def MenuGestionCasaInversora():
    print("\n*****************************")
    print("********MENU GESTION CASA INVERSORA*********")
    print("*****************************")
    print("1. Crear Casa Inversora")
    print("2. Eliminar Casa Inversora")
    print("3. Modificar Informacion")
    print("4. Mostrar Informacion")
    print("5. Atras")


def MenuGestionCuenta():
    print("\n********************************")
    print("******MENU GESTION CUENTA******")
    print("*********************************")
    print("1. Crear Cuenta")
    print("2. Eliminar Cuenta")
    print("3. Informacion de la cuenta")
    print("4. Atras")


def MenuGestionEmpleado():
    print("\n********************************")
    print("******MENU GESTION EMPLEADO******")
    print("*********************************")
    print("1. Crear Empleado")
    print("2. Modificar Empleado")
    print("3. ELiminar Empleado")
    print("4. Atras")


# SUB MENU GESTION BANCO
def MenuBanco():
    varOpcion = 0
    while (varOpcion != 5):

        if (varOpcion == 1):
            crearBanco()
        if (varOpcion==2):
            EliminarBanco()
        if (varOpcion==3):
            ModificarBanco()
        if ( varOpcion==4):
            mostrasBanco()


        MenuGestionBanco()
        try:
            varOpcion = int(input('Ingrese su opcion: '))
            if (varOpcion < 0 or varOpcion > 5):
                print("\nDebe ingresar una opcion valida")
                varOpcion = 0
            var_error = int(varOpcion)
        except:
            print("Debe ingresar un valor numerico")
            varOpcion = 0


# SUB MENU GESTION CLIENTE
def MenuCliente():
    varOpcion = 0
    while varOpcion != 5:

        if varOpcion == 1:
            crearCliente()
        if varOpcion == 2:
            añadirCuentaCliente()
        if varOpcion == 3:
            eliminarCuenta()
        if varOpcion == 4:
            mostrarCuenta()

        MenuGestionCliente()
        try:
            varOpcion = int(input('Ingrese su opcion: '))
            if (varOpcion < 0 or varOpcion > 4):
                print("\nDebe ingresar una opcion valida")
                varOpcion = 0
            var_error = int(varOpcion)
        except:
            print("Debe ingresar un valor numerico")
            varOpcion = 0


# SUB MENU GESTION CASA INVERSIONISTA
def MenuCasaI():
    varOpcion = 0
    while (varOpcion != 5):

        if (varOpcion == 1):
            crearCasa()
        if (varOpcion == 2):
            eliminarCasa()
        if (varOpcion == 3):
            modificarCasa()
        if (varOpcion == 4):
            mostrarInformacionCasa()

        MenuGestionCasaInversora()
        try:
            varOpcion = int(input('Ingrese su opcion: '))
            if (varOpcion < 0 or varOpcion > 5):
                print("\nDebe ingresar una opcion valida")
                varOpcion = 0
            var_error = int(varOpcion)
        except:
            print("Debe ingresar un valor numerico")
            varOpcion = 0


def existeCasaInversionista(parClave):
    exist = False
    for Casa_Inversionista in lista_Casas_Inversionistas:
        if (parClave == Casa_Inversionista.getClave()):
            exist = True
        return exist


def crearCasa():
    varNombreCasa = input('Ingresa el nombre de la casa de inversionistas: ')
    varClave = int(input('Ingresa la clave: '))
    varPorcentaje = float(input('Ingresa el porcentaje de retorno: '))
    varMonto = int(input('Ingresa el monto: '))
    varPlazo = float(input('Ingresa los plazos: '))
    varNivelRiesgo = float(input('Ingresa el nivel del riesgo: '))

    aux = existeCasaInversionista(varClave)
    if (aux == True):
        print("Esta casa inversionista ya existe")
    else:
        lista_Casas_Inversionistas.append(
            Casa_Inversionista(varNombreCasa, varClave, varPorcentaje, varMonto, varPlazo, varNivelRiesgo))


def eliminarCasa():
    varClave = int(input('Ingresa la clave de la casa de inversionistas: '))
    aux = existeCasaInversionista(varClave)
    if (aux == True):
        for Casa_Inversionista in lista_Casas_Inversionistas:
            if (varClave == Casa_Inversionista.getClave()):
                varPosicion = lista_Casas_Inversionistas.index(Casa_Inversionista)
        lista_Casas_Inversionistas.pop(varPosicion)
        print("Casa de inversionistas eliminada con exito")
    else:
        print("No es posible eliminar casa inversionista debido a que la clave ingresada no existe")


def modificarCasa():
    varClave = int(input('Ingresa la clave de la casa de inversionistas: '))
    aux = existeCasaInversionista(varClave)
    if (aux == True):
        for Casa_Inversionista in lista_Casas_Inversionistas:
            if (varClave == Casa_Inversionista.getClave()):
                varPosicion = lista_Casas_Inversionistas.index(Casa_Inversionista)
                varAux = True
            else:
                varAux = False
            if (varAux == True):
                varNombreCasa = input('Ingresa el nuevo nombre de la casa de inversionistas: ')
                varClaveN = int(input('Ingresa la nueva clave: '))
                varPorcentaje = float(input('Ingresa el nuevo porcentaje de retorno: '))
                varMonto = int(input('Ingresa el nuevo monto: '))
                varPlazo = float(input('Ingresa el nuevo plazo: '))
                varNivelRiesgo = float(input('Ingresa el nuevo nivel de riesgo: '))
                lista_Casas_Inversionistas[varPosicion].setNombre(varNombreCasa)
                lista_Casas_Inversionistas[varPosicion].setClave(varClaveN)
                lista_Casas_Inversionistas[varPosicion].setPorcentajes(varPorcentaje)
                lista_Casas_Inversionistas[varPosicion].setMontos(varMonto)
                lista_Casas_Inversionistas[varPosicion].setPlazos(varPlazo)
                lista_Casas_Inversionistas[varPosicion].setNivel(varNivelRiesgo)
            else:
                print("Falla al intentar modificar informacion de casa inversionista")
    else:
        print("No es posible modificar casa inversionista debido a que la clave ingresada no existe")


def mostrarInformacionCasa():
    varClave = int(input('Ingresa la clave de la casa de inversionistas: '))
    aux = existeCasaInversionista(varClave)
    if (aux == True):
        for Casa_Inversionista in lista_Casas_Inversionistas:
            if (varClave == Casa_Inversionista.getClave()):
                varPosicion = lista_Casas_Inversionistas.index(Casa_Inversionista)
                varAux = True
            else:
                varAux = False

            if (varAux == True):
                lista_Casas_Inversionistas[varPosicion].mostrarDatos()
            else:
                print("Error al tratar de imprimir la informacion de la casa de inversionistas")
    else:
        print("No es posible mostrar la informacion de la casa inversionista debido a que la clave ingresada no existe")


# SUB MENU GESTION CUENTA
def MenuCuenta():
    print("Para poder crear una cuenta primero debe existir una casa de inversiones")
    varOpcion = 0
    while (varOpcion != 4):

        if (varOpcion == 1):
            crearCuenta()
        if (varOpcion == 2):
            eliminarCuenta()
        if (varOpcion == 3):
            mostrarCuentas()
        MenuGestionCuenta()
        try:
            varOpcion = int(input('Ingrese su opcion: '))
            if (varOpcion < 0 or varOpcion > 4):
                print("\nDebe ingresar una opcion valida")
                varOpcion = 0
            var_error = int(varOpcion)
        except:
            print("Debe ingresar un valor numerico")
            varOpcion = 0


def crearCuenta():
    varClave = int(input('Ingresa la clave de la casa de inversionistas: '))
    aux = existeCasaInversionista(varClave)
    if (aux == True):
        for Casa_Inversionista in lista_Casas_Inversionistas:
            if (varClave == Casa_Inversionista.getClave()):
                varPosicion = lista_Casas_Inversionistas.index(Casa_Inversionista)
                varAux = True
            else:
                varAux = False

            if (varAux == True):
                varMontoInicial = int(input('Ingresa el valor del monto inicial: '))
                varMinimo = int(input('Ingresa el valor del minimo: '))
                varPorcentaje = float(input('Ingresa el porcentaje: '))
                varSaldo = int(input('Ingresa el saldo: '))

                lista_Casas_Inversionistas[varPosicion].agregarCuenta(varMontoInicial, varMinimo, varPorcentaje,
                                                                      varSaldo)
            else:
                print(
                    "No es posible agregar una cuenta debido a que la clave ingresada no corresponde a ninguna casa de inversiones")
    else:
        print("No es posible crear una cuenta debido a que no existe una casa de inversiones con la clave recibida")


def eliminarCuenta():
    varClave = int(input('Ingresa la clave de la casa de inversionistas: '))
    aux = existeCasaInversionista(varClave)
    if (aux == True):
        for Casa_Inversionista in lista_Casas_Inversionistas:
            if (varClave == Casa_Inversionista.getClave()):
                varPosicion = lista_Casas_Inversionistas.index(Casa_Inversionista)
                varAux = True
            else:
                varAux = False

            if (varAux == True):
                varLongitudLista = lista_Casas_Inversionistas[varPosicion].mostrarDatosCuenta()
                if (varLongitudLista != 0):
                    varPosicionCuenta = int(input('Ingresa la posicion: '))
                    lista_Casas_Inversionistas[varPosicion].eliminarCuenta(varPosicionCuenta)
                    print("cuenta eliminada con exito")
                else:
                    print("La casa de inversionistas no tiene ninguna cuenta")
            else:
                print("No es posible eliminar la cuenta debido a que no se encontro la casa de inversionistas")
    else:
        print("No se encontro la casa de inversionistas")


def mostrarCuentas():
    varClave = int(input('Ingresa la clave de la casa de inversionistas: '))
    aux = existeCasaInversionista(varClave)
    if (aux == True):
        for Casa_Inversionista in lista_Casas_Inversionistas:
            if (varClave == Casa_Inversionista.getClave()):
                varPosicion = lista_Casas_Inversionistas.index(Casa_Inversionista)
                varAux = True
            else:
                varAux = False

            if (varAux == True):
                varLongitudLista = lista_Casas_Inversionistas[varPosicion].mostrarDatosCuenta()
                if (varLongitudLista == 0):
                    print("La casa de inversionistas no tiene ninguna cuenta")
            else:
                print("No existen cuentas en la casa de inversionistas ingresada")
    else:
        print("No se encontro la casa de inversionistas")


# SUB MENU GESTION EMPLEADOS
def MenuEmpleado():
    varOpcion = 0
    while (varOpcion != 4):

        if (varOpcion == 1):
            print("funcion aqui")

        MenuGestionBanco()
        try:
            varOpcion = int(input('Ingrese su opcion: '))
            if (varOpcion < 0 or varOpcion > 4):
                print("\nDebe ingresar una opcion valida")
                varOpcion = 0
            var_error = int(varOpcion)
        except:
            print("Debe ingresar un valor numerico")
            varOpcion = 0


# MENU PRINCIPAL
while (varOpcionMenuPrincipal != 6):

    if (varOpcionMenuPrincipal == 1):
        MenuBanco()
    if (varOpcionMenuPrincipal == 2):
        MenuCliente()
    if (varOpcionMenuPrincipal == 3):
        MenuCasaI()
    if (varOpcionMenuPrincipal == 4):
        MenuEmpleado()
    if (varOpcionMenuPrincipal == 5):
        MenuCuenta()
    MenuPrincipal()
    try:
        varOpcionMenuPrincipal = int(input('Ingrese su opcion: '))
        if (varOpcionMenuPrincipal < 0 or varOpcionMenuPrincipal > 6):
            print("\nDebe ingresar una opcion valida")
            varOpcionMenuPrincipal = 0
        var_error = int(varOpcionMenuPrincipal)
    except:
        print("Debe ingresar un valor numerico")
        varOpcionMenuPrincipal = 0


def crearCliente():
    nombre = input('Ingrese nombre del cliente')
    usuario = input('Ingrese nombre de usuario')
    identificacion = input('Ingrese su identificacion')

    for cliente in lista_cliente:
        if usuario == cliente.getUsuario():
            print('El usuario ya existe, intente con otro.')
            return

    lista_cliente.append(Cliente(nombre, usuario, identificacion))

def añadirCuentaCliente():
    usuario = input('Ingrese usuario para crear un cuenta')

    for cliente in lista_cliente:
        if usuario == cliente.getUsuario():
            monto_inicial = int(input('Ingrese monto inicial de la cuenta:'))
            minimo = int(input('Ingrese minimo:'))
            porcentaje = int(input('Porcentaje:'))
            saldo = int(input('Saldo de la cuenta:'))

            cliente.añadir_cuenta(monto_inicial, minimo, porcentaje, saldo)
            return

def eliminarCuenta():
    id_cuenta = int(input('Ingrese el id de la cuenta'))

    for cliente in lista_cliente:
        for cuenta in len(cliente.lista_cuentas):
            if id_cuenta == cuenta.id:
                cliente.eliminar_cuenta(id_cuenta)

def mostrarCuenta():
    usuario = input('Ingrese usuario para crear un cuenta')

    for cliente in lista_cliente:
        if usuario == cliente.getUsuario():
            cliente.mostrar_cuenta()