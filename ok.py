import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sys
from keras.models import load_model
import cv2
import numpy as np
from deepf import openc
from deepf1 import opencam
from deepf1 import playmusic
from deepf1 import stopmusic
import pygame
import time

def showloadingscreen():
    loading_screen = tk.Toplevel()
    loading_screen.title("Loading")
    loading_screen.geometry("400x100")
    loading_screen.resizable(False, False)
    loading_screen.configure(bg="black")
    loading_screen.overrideredirect(True)
    screen_width = loading_screen.winfo_screenwidth() # Get the screen width and height
    screen_height = loading_screen.winfo_screenheight()
    x = int(screen_width/2 - 150)     # Calculate the x and y coordinates to center the loading screen on the screen
    y = int(screen_height/2 - 50)
    loading_screen.geometry("+{}+{}".format(x, y)) # Set the position of the loading screen
    name_label = tk.Label(loading_screen, text=" EMOTION BASED \n MUSIC RECOMMENDATION ", font=("AkiraExpanded-SuperBold", 20), fg="white", bg="black")
    name_label.pack(pady=1, anchor="center")
    label = tk.Label(loading_screen, text="Loading...", font=("8514oem", 12), fg="white", bg="black")
    label.pack(pady=1, anchor="center")
    loading_screen.update()
    time.sleep(3) # Simulate loading process
    loading_screen.destroy()
    time.sleep(0.5) #Delay after loading
    
class App:
    def __init__(self,master):
        self.master=master
        self.frames()

    def frames(self):
        #mainframe
        self.main=tk.Frame(self.master)
        self.main.config(bg='#152238')
        self.title=tk.Label(self.main,text="EMOTION BASED \n MUSIC RECOMMENDATION",font=('Garamond',45,'bold'), bg='#152238', fg = "#FFFFFF", justify="center")
        self.title.pack(pady=40)
        self.opencam = tk.Button(self.main,text="OPEN CAMERA", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=self.opencamera)
        self.opencam.pack(pady=10, padx=15, expand=True)
        self.o = tk.Button(self.main,text="SHOW GRAPH", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=self.graph)
        self.o.pack(pady=10, padx=15, expand=True)
        self.exit = tk.Button(self.main,text="EXIT", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=self.quit)
        self.exit.pack(pady=10, padx=15, expand=True)
        self.main.pack()
        #happyframe
        self.happy = tk.Frame(self.master)
        self.happy.config(bg='#152238')
        self.title=tk.Label(self.happy,text="YOU ARE HAPPY",font=('Garamond',45,'bold'), bg='#152238', fg = "#FFFFFF", justify="center")
        self.title.pack(pady=40)
        self.h1 = tk.Button(self.happy, text="ETHIRNEECHAL", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=lambda:self.play_happy_music("C:\\Users\\mridu\\OneDrive\\Documents\\PYTHON\\ethirneechal.mp3"))
        self.h1.pack(pady=10, padx=15, expand=True)
        self.h2 = tk.Button(self.happy, text="DANDANAKKA", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=lambda:self.play_happy_music("C:\\Users\\mridu\\OneDrive\\Documents\\PYTHON\\dandanakka.mp3"))
        self.h2.pack(pady=10, padx=15, expand=True)
        self.h3 = tk.Button(self.happy, text="CHIKKU BUKKU", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=lambda:self.play_happy_music("C:\\Users\\mridu\\OneDrive\\Documents\\PYTHON\\chikkubukku.mp3"))
        self.h3.pack(pady=10, padx=15, expand=True)
        self.h4 = tk.Button(self.happy, text="EN FRIEND AH POLA", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=lambda:self.play_happy_music("C:\\Users\\mridu\\OneDrive\\Documents\\PYTHON\\enfriendahpola.mp3"))
        self.h4.pack(pady=10, padx=15, expand=True)
        self.exit = tk.Button(self.happy,text="EXIT", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=self.quit)
        self.exit.pack(pady=10, padx=15, expand=True)
        self.backk= tk.Button(self.happy,text="BACK TO HOME", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=self.show_main)
        self.backk.pack(pady=10, padx=15, expand=True)
        self.happy.pack_forget()
        #sadframe
        self.sad = tk.Frame(self.master)
        self.sad.config(bg='#152238')
        self.title=tk.Label(self.sad,text="YOU ARE SAD",font=('Garamond',45,'bold'), bg='#152238', fg = "#FFFFFF", justify="center")
        self.title.pack(pady=40)
        self.sad1 = tk.Button(self.sad, text="KANAVE KANAVE", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=lambda:self.play_sad_music("C:\\Users\\mridu\\OneDrive\\Documents\\PYTHON\\kanavekanave.mp3"))
        self.sad1.pack(pady=10, padx=15, expand=True)
        self.sad2 = tk.Button(self.sad, text="MANNIPAAYA", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=lambda:self.play_sad_music("C:\\Users\\mridu\\OneDrive\\Documents\\PYTHON\\mannipaaya.mp3"))
        self.sad2.pack(pady=10, padx=15, expand=True)
        self.sad3 = tk.Button(self.sad, text="OH PENNE", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=lambda:self.play_sad_music("C:\\Users\\mridu\\OneDrive\\Documents\\PYTHON\\ohpenne.mp3"))
        self.sad3.pack(pady=10, padx=15, expand=True)
        self.sad4 = tk.Button(self.sad, text="YAARO YAARO", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=lambda:self.play_sad_music("C:\\Users\\mridu\\OneDrive\\Documents\\PYTHON\\yaaroyaaro.mp3"))
        self.sad4.pack(pady=10, padx=15, expand=True)
        self.exit = tk.Button(self.sad,text="EXIT", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=self.quit)
        self.exit.pack(pady=10, padx=15, expand=True)
        self.backk= tk.Button(self.sad,text="BACK TO HOME", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=self.show_main)
        self.backk.pack(pady=10, padx=15, expand=True)
        self.sad.pack_forget()
        #angryframe
        self.angry = tk.Frame(self.master)
        self.angry.config(bg='#152238')
        self.title=tk.Label(self.angry,text="YOU ARE ANGRY",font=('Garamond',45,'bold'), bg='#152238', fg = "#FFFFFF", justify="center")
        self.title.pack(pady=40)
        self.a1 = tk.Button(self.angry, text="THEEMAIDHANVELLUM", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=lambda:self.play_a_music("C:\\Users\\mridu\\OneDrive\\Documents\\PYTHON\\theemaidhanvellum.mp3"))
        self.a1.pack(pady=10, padx=15, expand=True)
        self.a2 = tk.Button(self.angry, text="NERUPPUDA", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=lambda:self.play_a_music("C:\\Users\\mridu\\OneDrive\\Documents\\PYTHON\\Neruppuda.mp3"))
        self.a2.pack(pady=10, padx=15, expand=True)
        self.a3 = tk.Button(self.angry, text="KARMATHEME", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=lambda:self.play_a_music("C:\\Users\\mridu\\OneDrive\\Documents\\PYTHON\\karmatheme.mp3"))
        self.a3.pack(pady=10, padx=15, expand=True)
        self.a4 = tk.Button(self.angry, text="EVANDIUNNA", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=lambda:self.play_a_music("C:\\Users\\mridu\\OneDrive\\Documents\\PYTHON\\evandiunna.mp3"))
        self.a4.pack(pady=10, padx=15, expand=True)
        self.exit = tk.Button(self.angry,text="EXIT", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=self.quit)
        self.exit.pack(pady=10, padx=15, expand=True)
        self.backk= tk.Button(self.angry,text="BACK TO HOME", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=self.show_main)
        self.backk.pack(pady=10, padx=15, expand=True)
        self.angry.pack_forget()
        #Surpiseframe
        self.surprise = tk.Frame(self.master)
        self.surprise.config(bg='#152238')
        self.title=tk.Label(self.surprise,text="YOU ARE SURPRISED",font=('Garamond',45,'bold'), bg='#152238', fg = "#FFFFFF", justify="center")
        self.title.pack(pady=40)
        self.s1 = tk.Button(self.surprise, text="Sirikkalam Parakkalam", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=lambda:self.play_music("C:\\Users\\mridu\\OneDrive\\Documents\\PYTHON\\sirikkalamparakkalam.mp3"))
        self.s1.pack(pady=10, padx=15, expand=True)
        self.s2= tk.Button(self.surprise, text="Yethi Yethi", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=lambda:self.play_music("C:\\Users\\mridu\\OneDrive\\Documents\\PYTHON\\yethiyethi.mp3"))
        self.s2.pack(pady=10, padx=15, expand=True)
        self.s3 = tk.Button(self.surprise, text="Vaathi Coming", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=lambda:self.play_music("C:\\Users\\mridu\\OneDrive\\Documents\\PYTHON\\vaathicoming.mp3"))
        self.s3.pack(pady=10, padx=15, expand=True)
        self.s4 = tk.Button(self.surprise, text="Kannamma", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=lambda:self.play_music("C:\\Users\\mridu\\OneDrive\\Documents\\PYTHON\\kannamma.mp3"))
        self.s4.pack(pady=10, padx=15, expand=True)
        self.exit = tk.Button(self.surprise,text="EXIT", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=self.quit)
        self.exit.pack(pady=10, padx=15, expand=True)
        self.backk= tk.Button(self.surprise,text="BACK TO HOME", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=self.show_main)
        self.backk.pack(pady=10, padx=15, expand=True)
        self.surprise.pack_forget()
        #Neutralframe
        self.neutral = tk.Frame(self.master)
        self.neutral.config(bg='#152238')
        self.title=tk.Label(self.neutral,text="YOU ARE NEUTRAL",font=('Garamond',45,'bold'), bg='#152238', fg = "#FFFFFF", justify="center")
        self.title.pack(pady=40)
        self.n1 = tk.Button(self.neutral, text="Pistah", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=lambda:self.play_n_music("C:\\Users\\mridu\\OneDrive\\Documents\\PYTHON\\pistah.mp3"))
        self.n1.pack(pady=10, padx=15, expand=True)
        self.n2 = tk.Button(self.neutral, text="Surviva", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=lambda:self.play_n_music("C:\\Users\\mridu\\OneDrive\\Documents\\PYTHON\\surviva.mp3"))
        self.n2.pack(pady=10, padx=15, expand=True)
        self.n3 = tk.Button(self.neutral, text="Polladha Ulagam", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=lambda:self.play_n_music("C:\\Users\\mridu\\OneDrive\\Documents\\PYTHON\\polladhaulagam.mp3"))
        self.n3.pack(pady=10, padx=15, expand=True)
        self.n4 = tk.Button(self.neutral, text="Mustafa", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=lambda:self.play_n_music("C:\\Users\\mridu\\OneDrive\\Documents\\PYTHON\\mustafa.mp3"))
        self.n4.pack(pady=10, padx=15, expand=True)
        self.exit = tk.Button(self.neutral,text="EXIT", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=self.quit)
        self.exit.pack(pady=10, padx=15, expand=True)
        self.backk = tk.Button(self.neutral,text="BACK TO HOME", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=self.show_main)
        self.backk.pack(pady=10, padx=15, expand=True)
        self.neutral.pack_forget()
        #fearframe
        self.fear = tk.Frame(self.master)
        self.fear.config(bg='#152238')
        self.title=tk.Label(self.fear,text="YOU ARE SCARED",font=('Garamond',45,'bold'), bg='#152238', fg = "#FFFFFF", justify="center")
        self.title.pack(pady=40)
        self.f1 = tk.Button(self.fear, text="Not Afraid", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=lambda:self.play_f_music("C:\\Users\\mridu\\OneDrive\\Documents\\PYTHON\\eminem.mp3"))
        self.f1.pack(pady=10, padx=15, expand=True)
        self.f2 = tk.Button(self.fear, text="Brave", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=lambda:self.play_f_music("C:\\Users\\mridu\\OneDrive\\Documents\\PYTHON\\wearethechampions.mp3"))
        self.f2.pack(pady=10, padx=15, expand=True)
        self.f3 = tk.Button(self.fear, text="Fearless", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=lambda:self.play_f_music("C:\\Users\\mridu\\OneDrive\\Documents\\PYTHON\\fearless.mp3"))
        self.f3.pack(pady=10, padx=15, expand=True)
        self.f4 = tk.Button(self.fear, text="Fight Song", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=lambda:self.play_f_music("C:\\Users\\mridu\\OneDrive\\Documents\\PYTHON\\rachel.mp3"))
        self.f4.pack(pady=10, padx=15, expand=True)
        self.exit = tk.Button(self.fear,text="EXIT", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=self.quit)
        self.exit.pack(pady=10, padx=15, expand=True)
        self.backk = tk.Button(self.fear,text="BACK TO HOME", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=self.show_main)
        self.backk.pack(pady=10, padx=15, expand=True)
        self.fear.pack_forget()

    def opencamera(self):
        emotion = opencam()
        if emotion:
            if emotion == 'happy':
                self.show_happy_frame()
            elif emotion == 'sad':
                self.show_sad_frame()
            elif emotion == 'angry':
                self.show_angry_frame()
            elif emotion == 'neutral':
                self.show_neutral_frame()
            elif emotion == 'surprise':
                self.show_surprise_frame()
            elif emotion=='fear':
                self.show_fear_frame()
            else:
                messagebox.showerror("ERROR", "No emotions were scanned")
        else:
            messagebox.showerror("ERROR", "No emotions were scanned")
    def graph(self): 
      openc()

    def quit(self):
        root.destroy()
        sys.exit()
        

    def show_main(self):
        self.happy.pack_forget()
        self.sad.pack_forget()
        self.neutral.pack_forget()
        self.angry.pack_forget()
        self.fear.pack_forget()
        self.surprise.pack_forget()
        self.main.pack()

    def show_happy_frame(self):
        self.main.pack_forget()
        self.happy.pack()

    def show_sad_frame(self):
        self.main.pack_forget()
        self.sad.pack()

    def show_angry_frame(self):
        self.main.pack_forget()
        self.angry.pack()

    def show_fear_frame(self):
        self.main.pack_forget()
        self.fear.pack()

    def show_neutral_frame(self):
        self.main.pack_forget()
        self.neutral.pack()

    def show_surprise_frame(self):
        self.main.pack_forget()
        self.surprise.pack()
        
    def play_happy_music(self,path):
        playmusic(path)
        self.stop= tk.Button(self.happy,text="STOP", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=self.stop_music)
        self.stop.pack(pady=10, padx=15, expand=True)
        self.back= tk.Button(self.happy,text="BACK", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=self.back6)
        self.back.pack(pady=10, padx=15, expand=True)
        self.pause = tk.Button(self.happy,text="PAUSE", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=self.pause_music)
        self.pause.pack(pady=10, padx=15, expand=True)
        self.resume = tk.Button(self.happy,text="RESUME", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=self.resume_music)
        self.resume.pack(pady=10, padx=15, expand=True)
        self.h1.pack_forget()
        self.h2.pack_forget()
        self.h3.pack_forget()
        self.h4.pack_forget()
        
    
    def play_sad_music(self,path):
        playmusic(path)
        self.stop= tk.Button(self.sad,text="STOP", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=self.stop_music)
        self.stop.pack(pady=10, padx=15, expand=True)
        self.back= tk.Button(self.sad,text="BACK", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=self.back5)
        self.back.pack(pady=10, padx=15, expand=True)
        self.pause = tk.Button(self.sad,text="PAUSE", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=self.pause_music)
        self.pause.pack(pady=10, padx=15, expand=True)
        self.resume = tk.Button(self.sad,text="RESUME", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=self.resume_music)
        self.resume.pack(pady=10, padx=15, expand=True)
        self.sad1.pack_forget()
        self.sad2.pack_forget()
        self.sad3.pack_forget()
        self.sad4.pack_forget()
    
    def play_a_music(self,path):
        playmusic(path)
        self.stop= tk.Button(self.angry,text="STOP", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=self.stop_music)
        self.stop.pack(pady=10, padx=15, expand=True)
        self.back= tk.Button(self.angry,text="BACK", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=self.back4)
        self.back.pack(pady=10, padx=15, expand=True)
        self.pause = tk.Button(self.angry,text="PAUSE", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=self.pause_music)
        self.pause.pack(pady=10, padx=15, expand=True)
        self.resume = tk.Button(self.angry,text="RESUME", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=self.resume_music)
        self.resume.pack(pady=10, padx=15, expand=True)
        self.a1.pack_forget()
        self.a2.pack_forget()
        self.a3.pack_forget()
        self.a4.pack_forget()
        
    def play_f_music(self,path):
        playmusic(path)
        self.stop= tk.Button(self.fear,text="STOP", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=self.stop_music)
        self.stop.pack(pady=10, padx=15, expand=True)
        self.back= tk.Button(self.fear,text="BACK", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=self.back3)
        self.back.pack(pady=10, padx=15, expand=True)
        self.pause = tk.Button(self.fear,text="PAUSE", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=self.pause_music)
        self.pause.pack(pady=10, padx=15, expand=True)
        self.resume = tk.Button(self.fear,text="RESUME", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=self.resume_music)
        self.resume.pack(pady=10, padx=15, expand=True)
        self.f1.pack_forget()
        self.f4.pack_forget()
        self.f3.pack_forget()
        self.f2.pack_forget()
        
    def play_n_music(self,path):
        playmusic(path)
        self.stop= tk.Button(self.neutral,text="STOP", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=self.stop_music)
        self.stop.pack(pady=10, padx=15, expand=True)
        self.back= tk.Button(self.neutral,text="BACK", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=self.back2)
        self.back.pack(pady=10, padx=15, expand=True)
        self.pause = tk.Button(self.neutral,text="PAUSE", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=self.pause_music)
        self.pause.pack(pady=10, padx=15, expand=True)
        self.resume = tk.Button(self.neutral,text="RESUME", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=self.resume_music)
        self.resume.pack(pady=10, padx=15, expand=True)
        self.n1.pack_forget()
        self.n4.pack_forget()
        self.n3.pack_forget()
        self.n2.pack_forget()
        
    def play_music(self,path):
        playmusic(path)
        self.stop= tk.Button(self.surprise,text="STOP", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=self.stop_music)
        self.stop.pack(pady=10, padx=15, expand=True)
        self.back= tk.Button(self.surprise,text="BACK", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=self.back1)
        self.back.pack(pady=10, padx=15, expand=True)
        self.pause = tk.Button(self.surprise,text="PAUSE", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=self.pause_music)
        self.pause.pack(pady=10, padx=15, expand=True)
        self.resume = tk.Button(self.surprise,text="RESUME", font=("Garamond",15), width=30, height=1, bg="#FFD1DC", fg="#000000", command=self.resume_music)
        self.resume.pack(pady=10, padx=15, expand=True)
        self.s1.pack_forget()
        self.s4.pack_forget()
        self.s3.pack_forget()
        self.s2.pack_forget()

    def back1(self):
        self.surprise_widgets = [self.stop, self.back,self.pause,self.resume]
        for widget in self.surprise_widgets:
            widget.pack_forget()
        self.s1.pack(pady=10, padx=15, expand=True)
        self.s2.pack(pady=10, padx=15, expand=True)
        self.s3.pack(pady=10, padx=15, expand=True)
        self.s4.pack(pady=10, padx=15, expand=True)
        
    def back2(self):
        self.neutral_widgets = [self.stop, self.back,self.pause,self.resume]
        for widget in self.neutral_widgets:
            widget.pack_forget()
        self.n1.pack(pady=10, padx=15, expand=True)
        self.n2.pack(pady=10, padx=15, expand=True)
        self.n3.pack(pady=10, padx=15, expand=True)
        self.n4.pack(pady=10, padx=15, expand=True)
        
    def back3(self):
        self.fear_widgets = [self.stop, self.back,self.pause,self.resume]
        for widget in self.fear_widgets:
            widget.pack_forget()
        self.f1.pack(pady=10, padx=15, expand=True)
        self.f2.pack(pady=10, padx=15, expand=True)
        self.f3.pack(pady=10, padx=15, expand=True)
        self.f4.pack(pady=10, padx=15, expand=True)
        
    def back4(self):
        self.angry_widgets = [self.stop, self.back,self.pause,self.resume]
        for widget in self.angry_widgets:
            widget.pack_forget()
        self.a1.pack(pady=10, padx=15, expand=True)
        self.a2.pack(pady=10, padx=15, expand=True)
        self.a3.pack(pady=10, padx=15, expand=True)
        self.a4.pack(pady=10, padx=15, expand=True)

    def back5(self):
        self.sad_widgets = [self.stop, self.back,self.pause,self.resume]
        for widget in self.sad_widgets:
            widget.pack_forget()
        self.sad1.pack(pady=10, padx=15, expand=True)
        self.sad2.pack(pady=10, padx=15, expand=True)
        self.sad3.pack(pady=10, padx=15, expand=True)
        self.sad4.pack(pady=10, padx=15, expand=True)
        
    def back6(self):
        self.happy_widgets = [self.stop, self.back,self.pause,self.resume]
        for widget in self.happy_widgets:
            widget.pack_forget()
        self.h1.pack(pady=10, padx=15, expand=True)
        self.h2.pack(pady=10, padx=15, expand=True)
        self.h3.pack(pady=10, padx=15, expand=True)
        self.h4.pack(pady=10, padx=15, expand=True)

    def stop_music(self):
        stopmusic()
        self.stop.pack_forget()
        self.pause.pack_forget()
        self.resume.pack_forget()
        
    def pause_music(self):
     pygame.mixer.music.pause()

    def resume_music(self):
     pygame.mixer.music.unpause()

root =tk.Tk()
root.withdraw()
showloadingscreen()
root.deiconify()
app=App(root)
root.title("MUSIC PLAYER")
root.geometry("1000x500")
root.configure(bg='#152238')
root.mainloop()