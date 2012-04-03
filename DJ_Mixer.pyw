from tkinter import *
from sound_panel import *
import pygame.mixer
import os

app = Tk()
app.title("Head First Mix")

mixer = pygame.mixer
mixer.init()

dirList = os.listdir(".")
for fname in dirList:
    if fname.endswith(".wav"):
        panel = SoundPanel(app, mixer, fname)
        panel.pack()
def shutdown():
    track.stop()
    app.destroy()


app.protocol("WM_DELETE_WINDOW", shutdown)
app.mainloop()

