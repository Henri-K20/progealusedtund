from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def tervita():
    tervitus = "Tere, " + nimi.get()
    messagebox.showinfo(message=tervitus)

raam = Tk()
raam.title("Rimi Greeting")
raam.geometry("300x100")

#tektstikasti silt
silt = ttk.Label(raam,text="Nimi")
silt.place(x=5,y=5)

#tekstikast
nimi = ttk.Entry(raam)
nimi.place(x=70,y=5,width=150)

#greeting nupp
nupp = ttk.Button(raam,text="Customer greeting", command=tervita)
nupp.place(x=70,y=40,width=150)

#render
raam.mainloop()