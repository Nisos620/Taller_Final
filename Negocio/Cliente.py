class Cliente:
    def __init__(self,nombre,usuario,identificacion):
        self.nombre= nombre
        self.usuario= usuario
        self.identificacion= identificacion

    def getNombre(self):
        return self.nombre

    def getUsuario(self):
        return self.usuario

    def getIdentificacion(self):
        return self.identificacion

    def setnombre(self,nombre):
        self.nombre=nombre

    def setUsuario(self, usuario):
        self.usuario=usuario

    def setIdentificacion(self,identificacion):
        self.identificacion=iden tificacionpro