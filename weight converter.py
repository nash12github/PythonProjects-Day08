#importing tkinter module
import tkinter as tk
from tkinter import *

window=Tk()#creating a window
window.title("Code Global")#title of the window
window.geometry("500x500")#geometry of the window
#create a label
Label(window,text="WEIGHT CONVERTER",font=("Arial", 20 ),bg="brown",fg='pink').pack()

kg=tk.IntVar()#kg is integer type

def convert_to_gram():
    kg1=kg.get() #getting the value
    gram = float(kg1)*1000 #convert to float
    Label(window,text="This weight in grams would be",font=("Arial", 12 )).pack()
    Label(window,text=gram,bg="green").pack()

def convert_to_ounce():
    kg1=kg.get()#getting the value
    ounce = float(kg1)*35.274#convert to float
    Label(window,text="This weight in ounce would be",font=("Arial", 12 )).pack()
    Label(window,text=ounce,bg="green").pack()

def convert_to_pound():
    kg1=kg.get()#getting the value
    pound = float(kg1)*2.20462#convert to float
    Label(window,text="This weight in pound would be",font=("Arial", 12 )).pack()
    Label(window,text=pound,bg="green").pack()

Label(window,text="Enter the weight in Kgs",font=("Arial", 14 )).pack()
Entry(window,textvariable=kg).pack()#entry field
#creating buttons
Button(window,text="Convert to Gram",bg="grey",command=convert_to_gram).pack()
Button(window,text="Convert to Ounce",bg="grey",command=convert_to_ounce).pack()
Button(window,text="Convert to Pound",bg="grey",command=convert_to_pound).pack()

window.mainloop()
