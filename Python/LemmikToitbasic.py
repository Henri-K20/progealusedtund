valikud = ["makaron", "kiluvõileib", "hakklihakaste"]
valik = ""

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
        input("Seda ei ole valikus! Vajuta enter, et uuesti valida...\n:")
