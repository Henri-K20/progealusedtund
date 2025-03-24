valikud = ["makaron", "kiluvõileib", "hakklihakaste"]
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
    if valik in valikud:
        if valik == "makaron":
            print("Sinu lemmiksöök on paljas makaron, nõme")
        elif valik == "kiluvõileib":
            print("Ohh, eesti värk, naiss")
        elif valik == "hakklihakaste":
            print("Eh, kinda mid")
        break
    else:
        if i == 0:
            print("ok, kui sa midagi ei taha siis aidaa!")
            break
        input("Seda ei ole valikus! Vajuta enter, et uuesti valida...\n:")
        i -= 1