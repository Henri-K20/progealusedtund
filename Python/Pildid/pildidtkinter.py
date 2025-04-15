from tkinter import *

raam = Tk()
raam.title("Pildid")
tahvel = Canvas(raam,width=600,height=600,background="white")
tahvel.grid

hiinlane = PhotoImage(file="rice.png")
emoji = PhotoImage(file="nimetu.png")
img = tahvel.create_image(300, 300, image=emoji,activeimage=hiinlane,anchor=CENTER)

tahvel.pack()
raam.mainloop()