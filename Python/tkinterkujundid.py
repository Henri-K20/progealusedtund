Atsykkel = True
age = 0
värv = ""
kujund = ""
kujundid = ["kolmnurk", "ruut", "ristkülik", "ring", "ovaal", "kaheksanurk"]

def kolmnurk():
    raam.title = "Kolmnurk!"
    tahvel.create_polygon(300,150,450,450,150,450,fill=värv)
    
def ruut():
    raam.title = "Ruut!"
    tahvel.create_polygon(150,150,450,150,450,450,150,450,fill=värv)
    
def ristkülik():
    raam.title = "Ristkülik!"
    tahvel.create_rectangle(150,275,450,325,fill=värv,outline=värv)
    
def ring():
    raam.title = "ring!"
    tahvel.create_oval(150,150,450,450,fill=värv,outline=värv)
    
def ovaal():
    raam.title = "ovaal!"
    tahvel.create_oval(150,100,450,500,fill=värv,outline=värv)
#def kaheksaanurk():

    

while Atsykkel:
    try:
        age = int(input("Sisestage oma vanus.\n:"))
    except ValueError:
        input("Väär andmetüüp! Vajutage enter, et uuesti proovida")
    else:
        if age < 3:
            print("Olete liiga noor ja ei saa kujundit joonistada!")
        else:
            Atsykkel = False

if Atsykkel != True:
    while värv == "":
        värv = input("Mis on teie lemmikvärv inglise keeles?\n:")
    while True:
        try:
            kujund = int(input("""
#########################
Mis on teie lemmikkujund?
0. kolmnurk
1. ruut
2. ristkülik
3. ring
4. ovaal
5. kaheksanurk
#########################
Sisestage kujundi number.
:"""))
        
        except ValueError:
            input("Väär andmetüüp! Vajutage enter, et uuesti proovida")
        else:
            if kujund < len(kujundid):
                
                from tkinter import *
                raam = Tk()
                tahvel = Canvas(raam,width=600,height=600)
                match kujund:
                    case 0:
                        kolmnurk()
                    case 1:
                        ruut()
                    case 2:
                        ristkülik()
                    case 3:
                        ring()
                    case 4:
                        ovaal()
                    case 5:
                        kaheksanurk()
                tahvel.create_text(300,300,text=str(age))
                tahvel.pack()
                raam.mainloop()
            else:
                input("Valik ei eksisteeri! Vajutage enter, et uuesti proovida")
                
    
    
    
   

                




