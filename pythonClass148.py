#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 18:16:22 2023

@author: shauryalunkad
"""

from tkinter import *
import random

root=Tk()
root.title("luck friend Wheel")
root.geometry("400x400")


list1 = ["James" , "Isabella" , "Sophia" , "Oliver" , "Peter"]
print(list1)

def random_number():
    random_no = random.randint(0,4)
    print(random_no)
    random_lucky_friend = list1[random_no]
    print("your lucky friend is: " + random_lucky_friend)
    
btn1 = Button(root)
btn1 = Button(root, text="Who is your Lucky Friend?  ", command = random_number)
btn1.place(relx = 0.5,rely = 0.5, anchor = CENTER)



root.mainloop()


