import pygame
import tkinter as tkr 
from tkinter.filedialog import askdirectory
import os

#Creating Window
musicplayer = tkr.Tk()

musicplayer.title("Music Player")

#Diamension of window
musicplayer.geometry('450x350')#use x not * for show geometry.

#user select the directory where all songs present.
directory = askdirectory()

#set or change this directory to current directory using chdir() function. 
os.chdir(directory)

#creating song list usind listdir() method.
songlist = os.listdir()

playlist = tkr.Listbox(musicplayer, font = "Cambria 14 bold" , bg = "cyan2" , selectmode = tkr.SINGLE) #We pass some perameter in listbox as font which is related to font style bg is background color and selectmode is tkr.SINGLE means we want only one track at one time.

#insert songs in playlist form songlist using for loop.
for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos = pos + 1

#initializatiom methods of pygame.
pygame.init()
pygame.mixer.init()


#function for play music
def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))#line define user select the song and now set it to playlist and set it active.
    var.set(playlist.get(tkr.ACTIVE))# set music for play finally.
    pygame.mixer.music.play()# for play music.

#function for stop music
def ExitMusicPlayer():
    pygame.mixer.music.stop()#pygame has predefine fun fo stop music.

#fun for pause music
def pause():
    pygame.mixer.music.pause()

#fun for resume music 
def resume():
    pygame.mixer.music.unpause()

#creating button
Button_play = tkr.Button(musicplayer, height=3, width=5, text="Play Music", font="Cambria 14 bold", command=play, bg="lime green", fg="black")#fg stand for text color.
Button_stop = tkr.Button(musicplayer, height=3, width=5, text="Stop Music", font="Cambria 14 bold", command=ExitMusicPlayer, bg="red", fg="black")
Button_pause = tkr.Button(musicplayer, height=3, width=5, text="Pause Music", font="Cambria 14 bold", command=pause, bg="yellow", fg="black")
Button_resume = tkr.Button(musicplayer, height=3, width=5, text="Resume Music", font="Cambria 14 bold", command=resume, bg="blue", fg="black")

Button_play.pack(fill="x")#pack is a method of tkinter which pack our button in a box. fill="x" means button fill complete window.
Button_stop.pack(fill="x")
Button_pause.pack(fill="x")
Button_resume.pack(fill="x")

playlist.pack(fill="both", expand='yes')

#Display Current Song title
var = tkr.StringVar()
songtitle = tkr.Label(musicplayer, font="Cambria 14 bold", textvariable=var)
songtitle.pack()

musicplayer.mainloop()#By using this we continue our command or loop at infinite until user click on close.