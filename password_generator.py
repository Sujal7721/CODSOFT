from tkinter import *;
from tkinter import ttk;
import string
import random;

def Gen_passowrd():
    pass_len = Length.get()
    low = string.ascii_lowercase
    upp = string.ascii_uppercase
    digit = string.digits
    symbol = "#%&\/^@!"
    all = low + symbol + digit + upp
    rn = random.sample(all,int(pass_len))
    password = "".join(rn)
    label.config(text = password)
    

screen = Tk()
screen.title("Password Generator")
screen.geometry("300x300")
screen.config(bg = "yellow")

list_length = [5,6,7,8,9,10]
Length = StringVar();


length_p = ttk.Combobox(screen,value = list_length,textvariable = Length,font = ("Time New Roman",20))
length_p.place(x = 250,y = 80,height = 50,width = 19)

label = Label(screen,text = "",font = ("Time New Roman",15))
label.place(x = 50,y = 80,height = 50,width = 200)

button_gen = Button(screen,bg = "green",font = ("Time New Roman",10),text = "Generate",command = Gen_passowrd)
button_gen.place(x = 100,y = 150,height = 30,width = 100)

screen.mainloop()
