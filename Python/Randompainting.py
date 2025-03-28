from random import randint
from turtle import *
size = 100
outer = size*3.2

def kujundmatch(x):
    match x:
        case 1|2|3|4|5:
            for i in range(4):
                fd(size)
                lt(90)
        case 6|7|8|9|10:
            circle(size)
        case 11|12|13|14|15:
            for i in range(3):
                fd(size)
                lt(120)
        case 16|17|18|19|20:
            for i in range(6):
                fd(size)
                lt(60)
arv = 0
randarv = randint(1,20)
print(randarv)
while True:
    try:
        arv = int(input("Sisestage arv vahemikus 1-20.\n:"))
    except ValueError:
        print("Väär sisestus!")
    else:
        if 1 <= arv <= 20:
            break
        else:
            print("Arv peab olema vahemikus 1-20!")

match arv:
    case 1|6|11|16:
        color("Red")
    case 2|7|12|17:
        color("Yellow")
    case 3|8|13|18:
        color("Green")
    case 4|9|14|19:
        color("Blue")
    case 5|10|15|20:
        color("Black")

begin_fill()
kujundmatch(arv)
end_fill()

if arv == randarv:
    color("Black")
    width(5)
    kujundmatch(arv)
exitonclick()