from django.db import models

# Create your models here.
class Usuario(models.Model):
    nick = models.CharField(primary_key=True,max_length=20)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    contrasena = models.CharField(max_length=45)

    def __str__(self):
        return f"{self.nombre}{self.apellido}"
    
class Cancion(models.Model):
    id = models.AutoField(primary_key=True)
    bitrate = models.IntegerField()
    genero = models.CharField(max_length=20)
    autor = models.CharField(max_length=20)
    titulo = models.CharField(max_length=20)
    fecha = models.DateTimeField()
    duracion = models.TimeField()
    usuario_nick = models.ForeignKey(Usuario, on_delete=models.CASCADE)
