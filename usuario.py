
class Usuario:

    def Usuario(self,pNombre=None,pApellido=None,pFechaNacimiento=None,pIdEmpleado=None,pFechaIngreso=None):

        self.nombre = pNombre
        self.apellido = pApellido
        self.fechaNacimiento = pFechaNacimiento
        self.idEmpleado = pIdEmpleado
        self.fechaIngreso = pFechaIngreso


    def getNombre(self):

        return self.nombre

    def setNombre(self,pNombre):

        self.nombre = pNombre

    def getApellido(self):

        return self.apellido

    def setApellido(self,pApellido):

        self.apellido = pApellido

    def getFechaNacimiento(self):

        return self.fechaNacimiento

    def setFechaNacimiento(self,pFechaNacimiento):

        self.fechaNacimiento = pFechaNacimiento

    def getIdEmpleado(self):

        return self.idEmpleado

    def setIdEmpleado(self,pIdEmpleado):

        self.idEmpleado = pIdEmpleado
