from tkinter import *
from tkinter import ttk

raam = Tk()
raam.title("klahvistik")

kood = ttk.Entry(raam).grid(row=0,column=0,columnspan=3,rowspan=1,padx=5,pady=5,sticky=(N,W,E))

rida = 1
tulp = 0
arvNupul = 1

while arvNupul < 10:
    ttk.Button(raam,text=str(arvNupul)).grid(row=rida,column=tulp,padx=5,pady=5)
    
    if arvNupul % 3 == 0:
        rida += 1
        tulp = 0
    else:
        tulp+=1
    arvNupul+=1

ttk.Button(raam, text="*").grid(row=4,column=0,padx=5,pady=5)
ttk.Button(raam, text="0").grid(row=4,column=1,padx=5,pady=5)
ttk.Button(raam, text="#").grid(row=4,column=2,padx=5,pady=5)



raam.mainloop()