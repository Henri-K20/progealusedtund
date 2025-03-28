from random import randint
from turtle import *
size = 100
arv = 0
nimi = ""
#ruut, ring, kolmnurk, kuusnurk and  ristkülik, romb, rööpkülik
randarv = randint(1,42)
print(randarv)

def kujundmatch(x):
    match x:
        case 1|2|3|4|5|6:
            for i in range(4): #ruut
                fd(size)
                lt(90)
        case 7|8|9|10|11|12: #ring
            circle(size)
        case 13|14|15|16|17|18: #kolmnurk
            for i in range(3): 
                fd(size)
                lt(120)
        case 19|20|21|22|23|24: #kuusnurk
            for i in range(6):
                fd(size)
                lt(60)
        case 25|26|27|28|29|30: #ristkülik
            for i in range(2):
                fd(size)
                lt(90)
                fd(size/2)
                lt(90)
        case 31|32|33|34|35|36: #romb
            for i in range(4):
                lt(45)
                fd(size)
                lt(45)
        case 37|38|39|40|41|42:#rööpkülik
            for i in range(2):
                fd(size)
                lt(60)
                fd(size)
                lt(120)

def värvmatch(x):
    match x:
        case 1|7|13|19|25|31|37:
            color("Red")
        case 2|8|14|20|26|32|38:
            color("Yellow")
        case 3|9|15|21|27|33|39:
            color("Green")
        case 4|10|16|22|28|34|40:
            color("Blue")
        case 5|11|17|23|29|35|41:
            color("Orange")
        case 6|12|18|24|30|36|42:
            color("Black")

while True:
    try:
        arv = int(input("Sisestage arv vahemikus 1-42.\n:"))
        nimi = input("Sisestage oma nimi!\n:")
    except ValueError:
        print("Väär sisestus!")
    else:
        if 1 <= arv <= 42:
            try:
                int(nimi)
            except ValueError:
                break
            else:
                print("Nimi peab olema õige!")
        else:
            print("Arv peab olema vahemikus 1-42!")
värvmatch(arv)
begin_fill()
kujundmatch(arv)
end_fill()
up()
goto(size/3,size/4)
down()
color("White")
write(nimi)
up()
goto(0,0)
down()
if arv == randarv:
    width(5)
    color("Black")
    kujundmatch(arv)
    bgcolor("Pink")
exitonclick()