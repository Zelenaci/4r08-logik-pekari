#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:02:14 2019

@authors: KrySt
"""

#import tkinter as tk
from tkinter import Frame, Button, Radiobutton, Tk, W, N, NW, DISABLED, ACTIVE,Label, Canvas



class App():
    
    def __init__(self, master):
        self.hidden_btns = []
        self.play_btns = []
        self.score = []
        
        # vrchní skryté buttony 
        hiddenframe = Frame(master, width=320, height=320)
        hiddenframe.grid(column=0,row=0, sticky = W)
        for i in range(5):
            self.hidden_btns.append(Button(hiddenframe, bg="black", state=DISABLED))
            self.hidden_btns[i].grid(column=i,row=0,padx=1,pady=1)

        #label logik
        label=Label(master, text="Logik")
        label.grid(column=0,row=1,columnspan=5)


    
        # Herní buttony
        activeframe = Frame(master, width=320, height=320)
        activeframe.grid(column=0,row=2, sticky = W)
        for y in range(10):
            row = []
            for x in range(5):
                row.append(Button(activeframe, bg="grey"))
                row[x].grid(column=x,row=y,padx=1,pady=1)
            self.play_btns.append(row)
        
        
        #skore
        for y in range(10):
            self.score.append(Label(activeframe,text="0/0"))
            self.score[y].grid(column=6, row=y)
        
        
        
        
        
        
root = Tk()
app = App(root)
root.mainloop()