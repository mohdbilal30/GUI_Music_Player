# importing necessary modules
import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

#creating the application window 
musicplayer = tkr.Tk()

# Setting the title
musicplayer.title("Music Player")

# setting dimenstions for application window
musicplayer.geometry("450x350")

# asking for music directory
directory = askdirectory()

# setting the music directory to the cureent working directory
os.chdir(directory)

# creating song list
# os.listdir return a list containing the names of the entries
# in the directory given by the user
songlist = os.listdir()

# creating the playlist
playlist = tkr.Listbox(musicplayer,font = "Cambria 14 bold",bg="cyan2",selectmode=tkr.SINGLE)

# adding songs from songlist to playlist
for item in songlist:
    pos = 0
    playlist.insert(pos,item)
    pos = pos + 1
# intializing modules
pygame.init()
pygame.mixer.init()

# function for play button
def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()

# function of stop buttom
def ExitMusicPlayer():
    pygame.mixer.music.stop()

#function for pause buttom 
def pause():
    pygame.mixer.music.pause()

#function for resume buttom 
def resume():
    pygame.mixer.music.unpause()

#############Creating Buttons################

Button_play = tkr.Button(musicplayer,height=3,width=5,text="Play Music",font="Cambria 14 bold",command=play,bg="lime green",fg="black")
Button_stop = tkr.Button(musicplayer,height=3,width=5,text="Stop Music",font="Cambria 14 bold",command=ExitMusicPlayer,bg="red",fg="black")
Button_pause = tkr.Button(musicplayer,height=3,width=5,text="Pause Music",font="Cambria 14 bold",command=pause,bg="yellow",fg="black")
Button_resume = tkr.Button(musicplayer,height=3,width=5,text="Resume Music",font="Cambria 14 bold",command=resume,bg="skyblue",fg="black")

Button_play.pack(fill="x")
Button_stop.pack(fill="x")
Button_pause.pack(fill="x")
Button_resume.pack(fill="x")

playlist.pack(fill="both",expand="yes")

var = tkr.StringVar()
songtitle = tkr.Label(musicplayer,font="Cambria 12 bold",textvariable=var)
songtitle.pack()
musicplayer.mainloop()
