filmid = []
lemmikfilm = ""
vaste = "L"
film = "terminator"
film2 = "vanamehe film"

while vaste != "":
    vaste = input("Sisestage paar oma lemmikfilmi. Vajutage enter, kui rohkem ei ole.\n:").lower()
    if vaste != "":
        filmid.append(vaste)

while lemmikfilm == "":
    lemmikfilm = input("Sisestage oma kõige lemmikum film!\n:").lower()

if lemmikfilm in filmid:
    print(f"Ossa, oled {lemmikfilm} isegi kaks korda pannud!")
    
elif lemmikfilm not in filmid:
    print(f"Aga, kus on {lemmikfilm}?")

if film in filmid:
    print("You'll be back...")
    
if film2 in filmid:
    print("Aga kuš šu šnikurš on šiiš?")

match len(filmid):
    case _ if len(filmid) <=5:
        print("Sa ei vaata väga palju filme vist...")
    case _ if 5 < len(filmid) <= 10:
        print("Käid tihti kinos?")
    case _ if len(filmid) > 10:
        print("Siis pole mul siin midagi öelda härra movieguru, headaega")
    case _:
        print("Err...")