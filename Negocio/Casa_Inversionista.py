class Casa_Inversionista:
    def __init__(self,nombre,clave,porcentajes_retorno,montos,plazos,nivel_riesgo):
        self.nombre=nombre
        self.clave=clave
        self.porcentajes=porcentajes_retorno
        self.montos=montos
        self.plazos=plazos
        self.nivel=nivel_riesgo

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

    def setNombre(self,nombre):
        self.nombre=nombre

    def setClave(self,clave):
        self.clave=clave

    def setPorcentajes(self,porcentajes):
        self.porcentajes=porcentajes

    def setMontos(self,montos):
        self.montos=montos

    def setPlazos(self,plazos):
        self.plazos=plazos

    def setNivel(self,plazo):
        self.plazos=plazo