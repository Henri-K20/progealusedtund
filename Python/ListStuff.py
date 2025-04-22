# perekonnaliikmed = []
# while True:
#     vaste = input("Sisestage perekonnaliige. Kui ei ole, vajutage enter.\n:")
#     if vaste == "":
#         break
#     perekonnaliikmed.append(vaste)
# print(" ja ".join([", ".join(perekonnaliikmed[:-1]),(perekonnaliikmed[-1])]))
# 
# pikkused = []
# kokku = 0
# while True:
#     pikkus = input("Sisesta pereliikmete pikkused (cm), kui kõik vajutage enter.\n:")
#     if pikkus == "":
#         break
#     pikkused.append(float(pikkus))
# kokku = sum(pikkused)
# kokku /= len(pikkused)
# print("Teie pere keskmine pikkus on",round(kokku,2),"sentimeetrit.")

loomad = []
loop = True

loomadloop = True
while loop:
    vaste = input("Kas teil on perekonnaliikmeid? jah/ei\n:").lower()
    if vaste == "jah":
        while loomadloop:
            input("Sisestage liikmete lemmikloomanimed. Kui ei ole enam, vajutage enter.\n:")
            if loomad[-1] == "":
                loomadloop = False
                loomad.pop()
        loop = False
        print("Loomad on:", " ja ".join([", ".join(loomad[:-1]),loomad[-1]]))
    elif vaste == "ei":
        vaste = input("Kas teil on lemmikloomi? jah/ei\n:").lower()
        if vaste == "ei":
            print("Kahju, pesaleidjas on palju kasse kes tahaksid kodu.")
            loop = False
        elif vaste == "jah":
            loomad.append(input("Sisestage lemmikloomanimed. Kui ei ole enam, vajutage enter.\n:"))
            if loomad[-1] == "":
                loomad.pop()
                print("Loomad on:", " ja ".join([", ".join(loomad[:-1]),loomad[-1]]))


