from abc import ABC, abstractmethod

class Persona(ABC):

    @abstractmethod
    def __init__(self, cedula, nombre, apellido):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
    
    @abstractmethod
    def __str__(self):
        return " %s : %s, %s" % (str(self.cedula), self.apellido, self.nombre)
    
class Alumno(Persona):

    def __init__(self, cedula, nombre, apellido, carrera):
        super().__init__(cedula, nombre, apellido)
        self.carrera = carrera
    
    def __str__(self):
        return " %s : %s, %s, %s," % (str(self.cedula), self.apellido, self.nombre, self.carrera)    

if __name__ == '__main__':
    alumno = Alumno('4003745','Alvarenga','Fernando','Ing. en Informatica')
    print(alumno)
