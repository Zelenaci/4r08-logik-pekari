#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:02:14 2019

@authors: KrySt
"""

import webbrowser
from random import randint
from functools import partial
from tkinter import Frame, Button, Radiobutton, Tk, W, N, NW, DISABLED, ACTIVE,Label

ROWS = 10
COLUMNS = 5
COLORS = ["none","red", "lime", "blue", "yellow", "navy", "purple", "orange", "white"]

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
            self.hidden_btns.append(Button(hiddenframe, bg="black", state=DISABLED, width=4, height=2))
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
                row_btns[x].grid(column=x,row=y,padx=1,pady=1)
                row_stones.append(0)
            
            self.play_btns.append(row_btns)
            self.play_stones.append(row_stones)
        
    
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