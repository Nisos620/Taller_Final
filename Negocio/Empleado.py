class Empleado:
    def __init__(self,sucursalbanco,nombre,id,sueldo,aniostra,vacaciones,cargo):
        self.sucursalbanco=sucursalbanco
        self.nombre=nombre
        self.id=id
        self.sueldo=sueldo
        self.aniostrabajo=aniostra
        self.vacaciones=vacaciones
        self.cargo=cargo


    def getNombre(self):
        return self.nombre

    def getId(self):
        return self.id

    def getSueldo(self):
        return self.sueldo

    def getaniostrabajo(self):
        return self.aniostrabajo

    def getVacaciones(self):
        return self.vacaciones

    def getCargo(self):
        return self.cargo

    def setNombre(self, nombre):
        self.nombre = nombre

    def setId(self,id):
        self.id=id

    def setSueldo(self,sueldo):
        self.sueldo=sueldo

    def setaniostrabajo(self,aniostra):
        self.aniostrabajo=aniostra

    def setVacaciones(self,vacaciones):
        self.vacaciones=vacaciones

    def setCargo(self,cargo):
        self.cargo=cargo