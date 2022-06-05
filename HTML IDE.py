# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 11:43:44 2022

@author: ishar
"""

from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.minsize(650,650)
root.maxsize(650,650)
root.configure(bg="lavender")

open_img=ImageTk.PhotoImage(Image.open("open.png"))
save_img=ImageTk.PhotoImage(Image.open("save.png"))
run_img=ImageTk.PhotoImage(Image.open("run.png"))

label_file_name=Label(root, text="File Name")
label_file_name.place(relx=0.28, rely=0.03, anchor=CENTER)

input_file_name=Entry(root, bg="white")
input_file_name.place(relx=0.46, rely=0.03, anchor=CENTER)

my_text=Text(root, height=35, width=80, bg="white", fg="black")
my_text.place(relx=0.5, rely=0.55, anchor=CENTER)

root.mainloop()
