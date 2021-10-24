
class Persona():
    def __init__(self, ci, nombre, apellido, fecha_nac, edad, sexo, correo, tel):
        self.ci = ci
        self.nonbre = nombre
        self.apellido = apellido
        self.edad = edad
        self.fecha_nac = fecha_nac
        self.sexo = sexo
        self.correo = correo
        self.tel = tel


    # @staticmethod
    def vota(self): return self.edad > 17


class Estudiante(Persona):
    def __init__(self, ci, nombre, apellido, fecha_nac, edad, sexo, correo, tel, creditos, carrera, materias_cursando):
        super().__init__(ci, nombre, apellido, fecha_nac, edad, sexo, correo, tel)
        self.creditos = creditos
        self.carrera = carrera
        self.materias_cursando = materias_cursando
    
    def tiene_algun_credito(self): return self.creditos > 0

    

        


