from pygame import mixer
class Reproductor:
    #atributos
    archivo = None
    valor_volumen = None
    #constructor
    def __init__(self, archivo):
        self.archivo = archivo
        self.valor_volumen = 0
        mixer.init()
        mixer.music.load(archivo)

    def play(self):
        mixer.music.play()
        return "Reproduciondo Musica"
    
    def pause(self):
        mixer.music.pause()
        return "La musica se ha pausado"
    
    def stop(self):
        mixer.music.stop()
        return "La musica se detuvo"
    
    def volume(self,v):
        self.valor_volumen+= v
        if (self.valor_volumen >= 1):
            self.valor_volumen = 1
        elif (self.valor_volumen <= 0):
            self.valor_volumen = 0
        mixer.music.set_volume(self.valor_volumen)
        return "Definiendo volumen a {}".format(v)
    