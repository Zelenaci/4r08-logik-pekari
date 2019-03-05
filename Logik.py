#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:02:14 2019

@authors: KrySt
"""

#import tkinter as tk
from tkinter import Frame, Button, Radiobutton, Tk, W, N, NW, DISABLED, ACTIVE,Label



class App():
    
    def __init__(self,master):
        #hlavní okno
        frame = Frame(master)
        frame.grid()
        
        #vrchní skryté buttony 
        hiddenframe=Frame(master).grid(column=0,row=0)
        hidden_btns = []
        for i in range(5):
            hidden_btns.append(Button(hiddenframe, bg="black", state=DISABLED).grid(column=i,row=0,padx=1,pady=1))
        
        activeframe=Frame(master).grid(column=0,row=1)
        play_btns = []
        for y in range(10):
            row = []
            for x in range(5):
                row.append(Button(activeframe, bg="grey").grid(column=x,row=y,padx=1,pady=1))
            play_btns.append(row)
                
        
        
        
        
        
        
        
root = Tk()
app = App(root)
root.mainloop()