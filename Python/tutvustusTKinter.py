from tkinter import *

raam = Tk()
raam.title("tahvel")

tahvel = Canvas(raam,width=600,height=600)
#elemendid

#jooned
#tahvel.create_line(150,150,450,150,450,450,150,450,150,150,width=4,fill="green", arrow=LAST)

#ristkülik
#tahvel.create_rectangle(150,150,450,450,width=4,outline="red",fill="pink")

#hulknurk ehk polygon
#tahvel.create_polygon(150,150,150,450,450,450,width=4,outline="gray",fil="blue")

#ovaal
tahvel.create_oval(150,150,450,450,width=4,outline="blue",fill="cyan")

#text
tahvel.create_text(300,100,text="OMEGALUL!",fill="purple",)

tahvel.pack()
raam.mainloop()