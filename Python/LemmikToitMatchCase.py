valik = ""
i = 5

while True:
    valik = input("""
########################################
Sisestage oma lemmik toit siit valikust:
Makaron
Kiluvõileib
Hakklihakaste
########################################
:""").lower()
    if i == 0:
        print("ok, kui sa midagi ei taha siis aidaa!")
        break
    match valik:
        case "makaron":
            print("Sinu lemmiksöök on paljas makaron, nõme")
            break
        case "kiluvõileib":
            print("Ohh, eesti värk, naiss")
            break
        case "hakklihakaste":
            print("Eh, kinda mid")
            break
        case _:
            input("Seda ei ole valikus! Vajuta enter, et uuesti valida...\n:")
            i -= 1
