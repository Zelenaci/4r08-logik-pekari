#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:02:14 2019

@authors: KrySt
"""

import webbrowser
from random import randint
from functools import partial
from tkinter import Frame, Button, Radiobutton, Tk, W, N, NW, E, DISABLED, ACTIVE,Label,OptionMenu,StringVar

ROWS = 10
COLUMNS = 5
COLORS = ["none",
          "red",
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
        
        self.color_selected = 8
        self.round = 0
        
        # vrchní skryté buttony 
        hiddenframe = Frame(master, width=320, height=320)
        hiddenframe.grid(column=0,row=0, sticky = W)
        for x in range(COLUMNS):
            self.hidden_btns.append(Button(hiddenframe, bg="black", state=DISABLED, width=8, height=4))
            self.hidden_btns[x].grid(column=x,row=0,padx=1,pady=1)
            self.hidden_stones.append(0)

        #label logik
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
                row_btns.append(Button(activeframe, bg = "grey", width = 4, height = 2, command=partial(self.set_color, x, y, self.color_selected)))
                row_btns.append(Button(activeframe, bg = "grey", width = 8, height = 4, state = btn_state, command=partial(self.set_color, x, y, self.color_selected)))
                row_btns[x].grid(column=x,row=y,padx=1,pady=1)
                row_stones.append(0)
            
            self.play_btns.append(row_btns)
            self.play_stones.append(row_stones)
        
         # Vyber barvy
        colorframe = Frame(master,width=320,height=320)
        colorframe.grid(column=0,row=3,sticky= W)
        
        var1=StringVar(master)
        menu1=OptionMenu(colorframe,var1,*COLORS)
        menu1.grid(column=0,row=0,pady=5)
        menu1.config(width=4)
        var2=StringVar(master)
        menu2=OptionMenu(colorframe,var2,*COLORS)
        menu2.grid(column=1,row=0,pady=5)
        menu2.config(width=4)
        var3=StringVar(master)
        menu3=OptionMenu(colorframe,var3,*COLORS)
        menu3.grid(column=2,row=0,pady=5)
        menu3.config(width=4)
        var4=StringVar(master)
        menu4=OptionMenu(colorframe,var4,*COLORS)
        menu4.grid(column=3,row=0,pady=5)
        menu4.config(width=4)
        var5=StringVar(master)
        menu5=OptionMenu(colorframe,var5,*COLORS)
        menu5.grid(column=4,row=0,pady=5)
        menu5.config(width=4)
            
         #tlacitko nove hry
        newgame_btn = Button(master,command=self.new_game,text="Opakovat hru",bd=5,bg="red")
        newgame_btn.grid(column=0,row=4,padx=10,pady=10)
        
        #tlacitko dalsiho tahu
        
        turn_btn = Button(master,command=self.next_round,text="Potvrdit tah",bd=10,bg="lime")
        turn_btn.grid(column=1,row=2,padx=10,pady=10)
        
        
        # Skore
        for y in range(ROWS):
            self.score.append(Label(activeframe,text="-/-"))
            self.score[y].grid(column=6, row=y)
    
    def new_game(self):    
        # vrchní skryté buttony 
        for x in range(COLUMNS):
            self.hidden_btns[x].configure(bg = "black")
            self.hidden_stones[x] = randint(1, len(COLORS)-1)                 # Start from color [1], [0] = none color 
            
        for y in range(ROWS):
            # Skore
            self.score[y].configure(text="-/-")
            
            # Herní buttony
            btn_state = ACTIVE if ROWS-1-y == self.round else DISABLED
            for x in range(COLUMNS):
                self.play_btns[y][x].configure(state = btn_state, bg = "grey")
                self.play_stones[y][x] = 0
                
            
    def show_stones(self):
        for i in range(COLUMNS):
            self.hidden_btns[i].configure(bg = COLORS[self.hidden_stones[i]])
            
    def next_round(self):
        for i in range(COLUMNS):
            self.play_btns[ROWS-1-self.round][i].configure(state = DISABLED)
            pass
        
        if self.round+1 < ROWS:
            self.round += 1
            for i in range(COLUMNS):
                self.play_btns[ROWS-1-self.round][i].configure(state = ACTIVE)
            
        else:
            self.end_game("LOSE")
            
            
    def set_color(self, x, y, color):
        self.play_stones[y][x] = color
        self.play_btns[y][x].configure(bg = COLORS[color])
        self.check_colors()
        
    def check_colors(self):
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
            
    def end_game(self, state):
        self.show_stones()
        
        if state == "WIN":
            pass
        elif state == "LOSE":
            webbrowser.open("https://youtu.be/gH476CxJxfg")
            
class Jukebox():
    def __init__(self):
        self.played_win_songs = []
        self.played_lose_songs = []
        
        
root = Tk()
app = App(root)
app.new_game()
app.show_stones()
app.end_game("LOSE")
root.mainloop()