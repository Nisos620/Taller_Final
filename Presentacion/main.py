from Negocio.Casa_Inversionista import Casa_Inversionista

varOpcionMenuPrincipal = 0
listaCasaInversionistas = list()


def MenuPrincipal():
    print("\n*****************************")
    print("*******MENU PRINCIPAL********")
    print("*****************************")
    print("1. Gestion Banco")
    print("2. Gestion Cliente(s)")
    print("3. Gestion Casa Inversionista")
    print("4. Gestion Empleados")
    print("5. Salir")


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
    print("2. Modificar Informacion")
    print("3. Mostrar Informacion")
    print("4. Atras")


def MenuGestionCasaInversora():
    print("\n*****************************")
    print("********MENU GESTION CASA INVERSORA*********")
    print("*****************************")
    print("1. Crear Casa Inversora")
    print("2. Eliminar Casa Inversora")
    print("3. Modificar Informacion")
    print("4. Mostrar Informacion")
    print("5. Gestion Cuenta")
    print("6. Atras")


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
            print("funcion aqui")

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


# SUB MENU GESTION CASA INVERSIONISTA
def MenuCasaI():
    varOpcion = 0
    while (varOpcion != 6):

        if (varOpcion == 1):
            print("asdasd")

        MenuGestionCasaInversora()
        try:
            varOpcion = int(input('Ingrese su opcion: '))
            if (varOpcion < 0 or varOpcion > 6):
                print("\nDebe ingresar una opcion valida")
                varOpcion = 0
            var_error = int(varOpcion)
        except:
            print("Debe ingresar un valor numerico")
            varOpcion = 0


def crearCasaInversionista():
    varNombre = input('Ingrese nombre de la casa de inversionistas: ')
    varClave = int(input('ingrese la clave: '))
    varPorcentaje = float(input('Ingrese el porcentaje de retorno: '))
    varMonto = int(input('Ingrese el monto: '))
    varPlazos = float(input('Ingrese los plazos: '))
    varRiesgo = float(input('Ingrese el nivel de riesgo: '))
    objCasaInversionista = Casa_Inversionista(varNombre, varClave, varPorcentaje, varMonto, varPlazos, varRiesgo)
    listaCasaInversionistas.append(objCasaInversionista)


def eliminarCasaInversionista():
    varClave = int(input('ingrese la clave: '))


def modificarCasaInversionista():
    varClave = int(input('ingrese la clave: '))


def mostrarInformacionCasaInversionista():
    varClave = int(input('ingrese la clave: '))



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
while (varOpcionMenuPrincipal != 5):

    if (varOpcionMenuPrincipal == 1):
        MenuBanco()
    if (varOpcionMenuPrincipal == 2):
        MenuCliente()
    if (varOpcionMenuPrincipal == 3):
        MenuCasaI()
    if (varOpcionMenuPrincipal == 4):
        MenuEmpleado()

    MenuPrincipal()
    try:
        varOpcionMenuPrincipal = int(input('Ingrese su opcion: '))
        if (varOpcionMenuPrincipal < 0 or varOpcionMenuPrincipal > 5):
            print("\nDebe ingresar una opcion valida")
            varOpcionMenuPrincipal = 0
        var_error = int(varOpcionMenuPrincipal)
    except:
        print("Debe ingresar un valor numerico")
        varOpcionMenuPrincipal = 0
