from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def tervita():
    tervitus = "Tere, " + nimi.get()
    messagebox.showinfo(message=tervitus)

raam = Tk()
raam.title("Rimi Greeting")
#raam.geometry("300x100")

#tektstikasti silt
silt = ttk.Label(raam,text="Nimi")
silt.grid(column=0,row=0,padx=5,pady=5,sticky=(N,W))

#tekstikast
nimi = ttk.Entry(raam)
nimi.grid(column=1,row=0,padx=5,pady=5,sticky=(N,W,E))

#greeting nupp
nupp = ttk.Button(raam,text="Customer greeting", command=tervita).grid(column=1,row=1,padx=5,pady=5,sticky=(N,W,E,S))

raam.columnconfigure(1,weight=1)
raam.rowconfigure(1,weight=1)


#render
raam.mainloop()