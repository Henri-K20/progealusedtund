from turtle import *
fail = open("Andmed/turtlejuhis.txt")
andmed = []

for rida in fail:
    andmed.append(rida.split())
fail.close()

if andmed[0] != "edasi" or andmed[0] != "tagasi" or andmed[0] != "paremale" or andmed[0] != "vasakule":
    color(andmed[0])
    andmed.pop(0)

i = 0
while i < len(andmed):
    if andmed[i][0] == "edasi":
        forward(int(andmed[i][1]))
    elif andmed[i][0] == "tagasi":
        back(int(andmed[i][1]))
    elif andmed[i][0] == "paremale":
        right(int(andmed[i][1]))
    elif andmed[i][0] == "vasakule":
        left(int(andmed[i][1]))
    i+=1
exitonclick()