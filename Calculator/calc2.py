from tkinter import *

root = Tk()
root.title("DJ Calculator")

#Entry boxes, parameters(width, bg, fg, borderwidth, font, justify)
e = Entry(root, width = 50)
e.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)
ops = ""
last = 0
recent = 0

def button_clik(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_add():
    global ops
    global last
    last = int(e.get())
    e.delete(0, END)
    ops = "add"

def button_sub():
    global ops
    global last
    last = int(e.get())
    e.delete(0, END)
    ops = "sub"

def button_mult():
    global ops
    global last
    last = int(e.get())
    e.delete(0, END)
    ops = "mult"

def button_div():
    global ops
    global last
    last = int(e.get())
    e.delete(0, END)
    ops = "div"
    
def button_equal():
    global ops
    global recent
    global last
    recent = int(e.get())
    e.delete(0, END)
    if ops == "add":
        ans =   last+recent
    if ops == "sub":
        ans = last-recent
    if ops == "mult":
        ans = last*recent
    if ops == "div":
        ans = last/recent
    e.insert(0, ans)
    last = ans
    
def button_clear():
    e.delete(0, END)
    
button_1 = Button(root, text = "1", padx = 30, pady = 20, command = lambda: button_clik(1))
button_2 = Button(root, text = "2", padx = 30, pady = 20, command = lambda: button_clik(2))
button_3 = Button(root, text = "3", padx = 30, pady = 20, command = lambda: button_clik(3))
button_4 = Button(root, text = "4", padx = 30, pady = 20, command = lambda: button_clik(4))
button_5 = Button(root, text = "5", padx = 30, pady = 20, command = lambda: button_clik(5))
button_6 = Button(root, text = "6", padx = 30, pady = 20, command = lambda: button_clik(6))
button_7 = Button(root, text = "7", padx = 30, pady = 20, command = lambda: button_clik(7))
button_8 = Button(root, text = "8", padx = 30, pady = 20, command = lambda: button_clik(8))
button_9 = Button(root, text = "9", padx = 30, pady = 20, command = lambda: button_clik(9))
button_0 = Button(root, text = "0", padx = 30, pady = 20, command = lambda: button_clik(0))
button_add = Button(root, text = "+", padx = 29, pady = 20, command = button_add)
button_sub = Button(root, text = "-", padx = 30, pady = 20, command = button_sub)
button_mult = Button(root, text = "X", padx = 29, pady = 20, command = button_mult)
button_div = Button(root, text = "/", padx = 30, pady = 20, command = button_div)
button_equal = Button(root, text = "=", padx = 29, pady = 20, command = button_equal)
button_clr = Button(root, text = "C", padx = 29, pady = 20, command = lambda: button_clear())


button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)
button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)
button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)
button_0.grid(row = 4, column = 0)
button_add.grid(row = 1, column = 3)
button_sub.grid(row = 2, column = 3)
button_mult.grid(row = 3, column = 3)
button_div.grid(row = 4, column = 3)
button_equal.grid(row = 4, column = 2)
button_clr.grid(row = 4, column = 1)
    

root.mainloop()
          


# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 09:27:45 2022

@author: Daniel Laserna
"""

