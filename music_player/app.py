import tkinter
import pygame
from tkinter import *
import os
from tkinter.filedialog import askdirectory

music_player = tkinter.Tk()
music_player.title("Music Player")
music_player.geometry("550x450")

directory = askdirectory()
os.chdir(directory) #it permits to change the current dir
song_list = os.listdir() #it returns the list of files song

music_list = tkinter.Listbox(music_player, font = "Helvetica 12 bold", bg="yellow", selectmode=tkinter.SINGLE)

for song in song_list:
    position = 0
    music_list.insert(position, song)
    position += 1

pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(music_list.get(tkinter.ACTIVE))
    var.set(music_list.get(tkinter.ACTIVE))
    pygame.mixer.music.play()
    
def stop():
    pygame.mixer.music.stop()
    
def pause():
    pygame.mixer.music.pause()
    
def unpause():
    pygame.mixer.music.unpause()



Button1 = tkinter.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="PLAY", command=play, bg="blue", fg="white")
Button2 = tkinter.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="STOP", command=play, bg="blue", fg="white")
Button3 = tkinter.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="PAUSE", command=play, bg="blue", fg="white")
Button4 = tkinter.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="UNPAUSE", command=play, bg="blue", fg="white")

var = tkinter.StringVar() 
song_title = tkinter.Label(music_player, font="Helvetica 12 bold", textvariable=var)

song_title.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
music_list.pack(fill="both", expand="yes")
music_player.mainloop()