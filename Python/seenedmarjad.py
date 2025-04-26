seened = ["lisa juurde", "pilvik", "kukeseen", "mürklid", "puravik", "võiseen"]
seenedSisu = []

marjad = ["lisa juurde", "mustikas", "jõhvikas", "vaarikas", "karusmari", "must sõstar"]
marjadSisu = []

midaOtsib = ""
valik = ""

while midaOtsib == "":
    midaOtsib = input("Kas te otsite seent või marja?\n->").lower()

if midaOtsib == "seent":
     while valik not in seened: 
        print("""########################
Sisestage valiku number.""")
        for index, seen in enumerate(seened):
            print(f"{index}: {seen.capitalize()}")
        
        try:
            valik = seened[int(input("\n->"))]
        except (IndexError, ValueError):
            input("Väär sisestus! Vajuta enterit, et uuesti proovida!\n->")
    
elif midaOtsib == "marja":
    while valik not in marjad: 
        print("""########################
Sisestage valiku number.""")
        for index, mari in enumerate(marjad):
            print(f"{index}: {mari.capitalize()}")
        
        try:
            valik = marjad[int(input("\n->"))]
        except (IndexError, ValueError):
            input("Väär sisestus! Vajuta enterit, et uuesti proovida!\n->")




