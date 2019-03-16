#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:02:14 2019

@authors: KrySt
"""

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
        for i in range(COLUMNS):
            self.hidden_btns.append(Button(hiddenframe, bg="black", state=DISABLED, width=4, height=2))
            self.hidden_btns[i].grid(column=i,row=0,padx=1,pady=1)

        #label logik
        label=Label(master, text="Logik")
        label.grid(column=0,row=1,columnspan=COLUMNS)

        # Herní buttony
        activeframe = Frame(master, width=320, height=320)
        activeframe.grid(column=0,row=2, sticky = W)
        for y in range(ROWS):
            row_btns = []
            row_stones = []
            btn_state = ACTIVE if ROWS-1-y == self.round else DISABLED
            
            for x in range(COLUMNS):
                row_btns.append(Button(activeframe, bg = "grey", width = 4, height = 2, state = btn_state, command=partial(self.set_color, x, y, self.color_selected)))
                row_btns[x].grid(column=x,row=y,padx=1,pady=1)
                row_stones.append(0)
            self.play_btns.append(row_btns)
            self.play_stones.append(row_stones)
        
        # Skore
        for y in range(ROWS):
            self.score.append(Label(activeframe,text="-/-"))
            self.score[y].grid(column=6, row=y)
    
    def new_game(self):
        self.hidden_stones = []      
        for i in range(COLUMNS):
            self.hidden_btns[i].configure(bg = "black")
            self.hidden_stones.append(randint(1, len(COLORS)-1))                   # Start from color [1], [0] = none color 
            
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
            self.show_stones()
            
    def set_color(self, x, y, color):
        self.play_stones[y][x] = color
        self.play_btns[y][x].configure(bg = COLORS[color])
        
    def check_colors(self, actual_round):
        position_color_counter = 0
        color_only_counter = 0
        
        for i in range(COLUMNS):
            if(self.play_stones[ROWS-1-self.round][i] == self.hidden_stones[i]):
                position_color_counter += 1
                
            if self.play_stones[ROWS-1-self.round][i] in self.hidden_stones:
                color_only_counter += 1
            
        
        
root = Tk()
app = App(root)
app.new_game()
root.mainloop()