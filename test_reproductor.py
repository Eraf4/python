from tkinter import *
from tkinter import ttk
from Reproductor import *

musica = Reproductor('wefere.mp3')

def play_musica():
    musica.volume(0.8)
    musica.play()

def puase_musica():
    musica.pause()

def volume_mas():
    musica.volume()

def volume_menos():
    musica.volume()

def stop_musica():
    musica.stop()

master = Tk()
master.geometry("200x200")

label = Label(master, text="Reproductor de música")
label.pack(pady=10)

btn_play = Button(master, text="▶", command = play_musica)
btn_play.pack(pady=10)
btn_pause = Button(master, text="⏸", command = puase_musica)
btn_pause.pack(pady=10)
btn_vol_mas = Button(master, text="➕", command = volume_mas)
btn_vol_mas.pack(pady=10)
btn_vol_menos = Button(master, text="➖", command = volume_menos)
btn_vol_menos.pack(pady=10)
btn_stop = Button(master, text="⏹", command = stop_musica)
btn_stop.pack(pady=10)

mainloop()