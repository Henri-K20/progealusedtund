from random import randint

player = 0
draakon = 0
panus = 0
summa = 0
while True:
    player = input("Palju raha soovite mängu panna?\n:")
    if not player.isnumeric:
        print("Peate sisestama positiivse täisarvu.")
    elif int(player) > 0:
        player = int(player)
        draakon+=player
        break
    else:
        print("Peate sisestama positiivse täisarvu.")

while True:
        print(f"Teil on {player}")
        panus = int(input("Palju soovite see mänguring panustada?\n:"))
        if int(panus) > int(player):
            print("Teil ei ole nii palju raha!")
            while int(panus) > int(player):
                panus = int(input("Sisestage rahaarv uuesti!\n:"))

        täringud = randint(3,18)
        küs = randint(3,18)
        if küs > täringud:
            vastus = "suurem"
        elif küs < täringud:
            vastus = "väiksem"
        arvamus = input(f"Mis arvate, kas {küs} on suurem või väiksem sellest mida veeretasin? (täringuid on 3 ja need on 6 külgsed!)\n:").lower()
        if arvamus == vastus:
            panus *= 2
            summa += panus
            draakon -= panus
            print(f"Vau! Võitsite {panus} draakonilt!")
        else:
            player -= panus
            draakon += panus
            print(f"Oi Ei! kaotasite {panus} draakonile!")
        if draakon <= 0:
            print("""
Tubli! Võitsid mängu!
--------------------
  VICTORY!      
--------------------
""")
            break
        elif player <= 0:
            print("""
Kurjam! Kaotasid!
--------------------
  Defeat!     
--------------------        
""")
            break
        edasi = input(f"Olete kokku võitnud {summa}, kas soovite võidud välja võtta ja lahkuda? (Teil on {player} ja draakonil on {draakon}) jah/ei\n:").lower()
        if edasi == "jah":
            player += summa
            print(f"Siin on sinu võidud, kokku on teil nüüd {player}, ootan sind ja sinu raha tagasi...")
            break
        elif edasi == "ei":
            print("Uuele ringile!")
