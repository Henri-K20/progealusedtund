loomad = []
vaste = ""
loom = "i"
while vaste == "":
    vaste = input("Kas teil on perekonnaliikmeid? jah/ei\n:").lower()
    if vaste == "jah":
        while loom != "":
            loom = input("Sisestage liikmete lemmikloomanimed. Kui ei ole enam, vajutage enter.\n:").capitalize()
            loomad.append(loom)
        loomad.pop()
        if len(loomad) == 1:
            print("Teie perekonnaliikme loom on", loomad[0]+".")
        else:
            print("Teie perekonnaliikmete loomad on", " ja ".join([", ".join(loomad[:-1]),loomad[-1]])+".")
    elif vaste == "ei":
        vaste = input("Kas teil on lemmikloomi? jah/ei\n:").lower()
        if vaste == "ei":
            print("Kahju, pesaleidjas on palju kasse kes tahaksid kodu.")
        elif vaste == "jah":
            while loom != "":
                loom = input("Sisestage lemmikloomanimed. Kui ei ole enam, vajutage enter.\n:").capitalize()
                loomad.append(loom)
            loomad.pop()
            if len(loomad) == 1:
                print("Teie loom on", loomad[0]+".")
            else:
                print("Teie loomad on", " ja ".join([", ".join(loomad[:-1]),loomad[-1]])+".")


