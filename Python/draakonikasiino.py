from random import randint

player = 0
draakon = 0
täringud = 0
panus = 0
while True:
    player = input("Palju raha soovite mängu panna?\n:")
    if not panus.isnumeric():
        print("Peate sisestama positiivse täisarvu.")
    elif int(panus) > 0:
        draakon+=player
        break

while True:
    if draakon <= 0:
        print("""
Tubli! Võitsid mängu!
--------------------
  VICTORY!      
--------------------
""")
        break
    else:
        panus = input("Palju soovite see mänguring panustada?\n:")
        if int(panus) > int(player):
            print("Teil ei ole nii palju raha!")
            while int(panus) > int(player):
                print("Sisestage rahaarv uuesti!\n:")
        arvamus = input("Mis arv tuleb täringutel kokku? (neid on 3 ja need on 6 külgsed!)\n:")
        vastus = randint(1,19)
        if arvamus == vastus:
            panus *= 2
            summa += panus
            print(f"Vau! Võitsite {panus}!")
        else:
            summa -= panus
            print(f"Oi Ei! kaotasite {panus} draakonile!")
        edasi = input(f"Olete kokku võitnud {summa}, kas soovite võidud välja võtta ja lahkuda? jah/ei\n:").lower()
        if edasi == "jah":
            player += summa
            print("Siin on sinu võidud, ootan sind ja sinu raha tagasi...")
            print(f"Teil on: {summa}")
            
        elif edasi == "ei":
            print("Uuele ringile!")
