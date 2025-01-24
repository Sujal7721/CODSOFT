from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import font

total_list = []

def add_list():
    list_data = my_Entry.get()
    my_Entry.delete(0,END)
    if list_data:
        total_list.append(list_data)
        mylist.insert(END,"  "+list_data)
    

def delet_line():
    selected_line = mylist.curselection()
    for i in reversed(selected_line):
        mylist.delete(i)

def clear_all():
    mylist.delete(0,END)


to = Tk()
to.title("To-Do List")
to.geometry("400x650")
to.config(bg = "azure2")

list_var = tk.StringVar()
image = tk.PhotoImage(file = "C:\garbage project.py\mini project\circle.png")
Photoimage = image.subsample(10,10)
frame = Frame(to,width = 320,height = 40,bg = "white")
frame.place(x = 5,y = 120)
frame1 = Frame(to,width = 700,height = 280,bd = 3)
frame1.pack(pady = (180,0))


label = Label(to,text = "TO-Do LIST",bg = "steelblue4",font = ("Time New Roman",20,"bold"))
label.place(x = 0,y = 20,height = 50,width = 400)

my_Entry = tk.Entry(frame,textvariable = list_var,font = ('calibre',20,'normal'),bd = 0)
# my_Entry.grid(row = 0,column = 0)
# my_Entry.pack(padx = 10,pady = 120,ipady = 5,ipadx = 10,)
my_Entry.place(x = 0,y = 0)


myscroll = Scrollbar(frame1)
myscroll.pack(side = RIGHT,fill = BOTH)


#listbox
mylist = Listbox(frame1,width = 400,height = 12,fg = "white",cursor = "hand2",bg = "steelblue4")
mylist.pack(side = LEFT,fill = BOTH,padx = 2)
listbox_font = font.Font(family = "Arial",size = 15)
mylist.config(font = listbox_font)
mylist.config(yscrollcommand = myscroll.set)
myscroll.config(command = mylist.yview)


Button_add = Button(to,text = "ADD",font = ("Time New Roman",20,"bold"),bg = "cadetblue",command = add_list)
Button_add.place(x = 320,y = 120,height = 40, width = 80)

Button_delet = tk.Button(to,image=Photoimage,bg = "azure2",command = delet_line)
Button_delet.place(x = 165,y = 500)

Button_clear = tk.Button(to,text = "Clear All",bg = "red",font = ("Time New Roman",13,"bold"),command = clear_all)
Button_clear.place(x = 158,y = 570,height = 40,width = 72)


to.mainloop()
