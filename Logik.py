#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:02:14 2019

@authors: KrySt
"""

import os
import webbrowser
from random import randint
from functools import partial
from tkinter import Frame, Button, Radiobutton, Tk, W, N, NW, E, DISABLED, NORMAL, Label, OptionMenu, StringVar

ROWS = 10
COLUMNS = 5
COLORS = ["red",
          "lime",
          "blue",
          "yellow",
          "navy",
          "purple",
          "orange",
          "white"]

class App():
    def __init__(self, master):
        self.hidden_btns = []
        self.play_btns = []
        self.score = []
        
        self.hidden_stones = []
        self.play_stones = []
        
        self.color_selected = "NONE"
        self.round = 0
        
        # vrchní skryté buttony 
        hiddenframe = Frame(master, width=320, height=320)
        hiddenframe.grid(column=0,row=0, sticky = W)
        for x in range(COLUMNS):
            self.hidden_btns.append(Button(hiddenframe, bg="black", state=DISABLED, width=4, height=2))
            self.hidden_btns[x].grid(column=x,row=0,padx=1,pady=1)
            self.hidden_stones.append(0)

        # label logik
        label=Label(master, text="Logik")
        label.grid(column=0,row=1,columnspan=COLUMNS)

       
        # Herní buttony
        activeframe = Frame(master, width=320, height=320)
        activeframe.grid(column=0,row=2, sticky = W)
        
        for y in range(ROWS):
            # Skore
            self.score.append(Label(activeframe,text="-/-"))
            self.score[y].grid(column=6, row=y)
            
            # Herní buttony
            row_btns = []
            row_stones = []
            for x in range(COLUMNS):
                row_btns.append(Button(activeframe, bg = "grey", width = 4, height = 2, 
                                       command=partial(self.set_color, x, y)))
                row_btns[x].grid(column=x,row=y,padx=1,pady=1)
                row_stones.append("NONE")
            
            self.play_btns.append(row_btns)
            self.play_stones.append(row_stones)
        
        # Vyber barvy
        colorframe = Frame(master,width=320,height=320)
        colorframe.grid(column=0,row=3,sticky= W)
        
        # všechna menu na výběr barev pro jednotlivé sloupce
        colorMenuVar = StringVar(colorframe)
        menu1 = OptionMenu(colorframe, colorMenuVar,*COLORS, command=self.save_color)
        menu1.grid(column=0,row=0,pady=5)
        menu1.config(width=4)
        
        # tlacitko nove hry
        newgame_btn = Button(colorframe,command=self.new_game,text="Opakovat hru",bd=3,bg="red")
        newgame_btn.grid(column=1,row=1,padx=10,pady=10)
        
        # tlacitko dalsiho tahu
        self.turn_btn = Button(colorframe,command=self.next_round,text="Potvrdit tah",bd=8,bg="lime")
        self.turn_btn.grid(column=1,row=0,padx=10,pady=10)
        
        label1=Label(colorframe,text="Barva/Pozice")
        label1.grid(column=2,row=0)
        
        # Skore
        for y in range(ROWS):
            self.score.append(Label(activeframe,text="-/-"))
            self.score[y].grid(column=6, row=y)
        
        self.new_game()    
    #______________________________________________________________________________________________#
    
    def new_game(self):    
        self.round = 0
        self.turn_btn.configure(state = NORMAL)
        
        # vrchní skryté buttony 
        for x in range(COLUMNS):
            self.hidden_btns[x].configure(bg = "black")
            self.hidden_stones[x] = randint(0, len(COLORS)-1)
            
        for y in range(ROWS):
            # Skore
            self.score[y].configure(text="-/-")
            
            # Herní buttony
            btn_state = NORMAL if ROWS-1-y == self.round else DISABLED
            for x in range(COLUMNS):
                self.play_btns[y][x].configure(state = btn_state, bg = "grey")
                self.play_stones[y][x] = 0
                       
    def show_stones(self):
        for i in range(COLUMNS):
            self.hidden_btns[i].configure(bg = COLORS[self.hidden_stones[i]])
            
    def next_round(self):
        self.check_score()
        
        for i in range(COLUMNS):
            self.play_btns[ROWS-1-self.round][i].configure(state = DISABLED)
        
        if self.round+1 < ROWS:
            self.round += 1
            for i in range(COLUMNS):
                self.play_btns[ROWS-1-self.round][i].configure(state = NORMAL)
            
        else:
            self.end_game("LOSE")
            
    def save_color(self, color):
        self.color_selected = COLORS.index(color)
    
    def set_color(self, x, y):
        if self.color_selected == "NONE":
            return
        
        self.play_stones[y][x] = self.color_selected
        self.play_btns[y][x].configure(bg = COLORS[self.color_selected])
        
    def check_score(self):
        position_color_counter = 0
        color_only_counter = 0
        
        for i in range(COLUMNS):
            if(self.play_stones[ROWS-1-self.round][i] == self.hidden_stones[i]):
                position_color_counter += 1
                
            if self.play_stones[ROWS-1-self.round][i] in self.hidden_stones:
                color_only_counter += 1
        color_only_counter -= position_color_counter
        
        self.score[ROWS-1-self.round].configure(text = "{}/{}".format(color_only_counter, position_color_counter))
        
        if position_color_counter == COLUMNS:
            self.end_game("WIN")
            
    def end_game(self, win_or_lose):
        self.show_stones()
        self.turn_btn.configure(state = DISABLED)
        jukebox.play_random(win_or_lose)
     
        
class Jukebox():
    def __init__(self):
        self.win_songs = []
        self.lose_songs = []
        
        self.load_songs("WIN")
        self.load_songs("LOSE")
    
    def load_songs(self, win_or_lose):
        song_files = ["jukebox\win_playlist.txt", "jukebox\lose_playlist.txt"]
        song_vars = [self.win_songs, self.lose_songs] 
        win_or_lose = 0 if win_or_lose == "WIN" else 1
         
        # File size check
        try:
            if os.path.getsize(song_files[win_or_lose]) > 4096:
                return
        except FileNotFoundError:
            return
        
        # Song loading
        with open(song_files[win_or_lose], "r") as f:
            while True:
                song = f.readline()
                if song:
                    song_vars[win_or_lose].append(song)
                else:
                    break
                    
    def play_random(self, win_or_lose):
        songs = self.win_songs if win_or_lose == "WIN" else self.lose_songs
        
        # No songs? Try to load it!
        if not songs:
            self.load_songs(win_or_lose)
        
        # Still nothing? Well, playlist may be corrupted, so enjoy the silence!
        if not songs:
            return
        
        song = songs.pop(randint(0,len(songs)-1))
        webbrowser.open(song)
        
      
root = Tk()
root.geometry("255x600+0+0")
app = App(root)
jukebox = Jukebox()
root.mainloop()