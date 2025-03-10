print("Tere!")
a = float(input("Mis on põranda ühe külje pikkus? cm" + "\n:"))
b = float(input("Mis on põranda teise külje pikkus? cm" + "\n:"))
s = a*b
print("Milliseid põrandaplaate soovite?")
while True:
    valik = input("""
########################
Sisestage soovitud valiku number.
1: ██
2: ░░
3: ║
4: ┌─┐
5: ▀▄
6: ░░
########################
:""")
    if valik == "1":
        print("██"*200)
        vhind = 0.5
        break
    elif valik == "2":
        print("░░"*200)
        vhind = 0.75
        break
    elif valik == "3":
        print("║"*200)
        vhind = 1
        break
    elif valik == "4":
        print("┌─┐"*200)
        vhind = 1.5
        break
    elif valik == "5":
        print("▀▄"*200)
        vhind = 2
        break
    elif valik == "6":
        print("░░"*200)
        vhind = 2.5
        break
    else:
        print("Väär sisestus!")
        input("Press enter continue...")
hind = vhind * s
vastus = input("Valisite number "+str(valik)+" mustri. Hind tuleb kokku: "+str(hind)+" Eurot. Kas soovite maksta? jah/ei"+"\n:").lower()
if vastus == "ei":
    hind *= 0.9
    vastus = input("Uus hind on: "+str(hind)+" eurot, kas soovite osta? jah/ei"+"\n:")
    if vastus == "ei":
        hind *= 0.9
        vastus = input("Viimane hind on: "+str(hind)+" eurot, kas soovite osta? jah/ei"+"\n:")
        if vastus == "ei":
            print("Head päeva. loodame, et tulevikus te ei ole nii vasesed!")
if vastus == "jah":
    print("Aitäh shoppamast! head päeva!")
    
    
