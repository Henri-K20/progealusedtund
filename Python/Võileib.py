from random import choice
sai = "[ , ,, '' ']"
kurk = "▄▄▄▄ ▄▄▄"
tomat = "( | ▌|██)"
bacon = '"~-,._.,-~"~-,.'
hind = 1.50
while True:
    isu = input("Kas teil on kõht tühi? jah/ei :").lower()
    if isu == "jah":
        while True:
            kokk = input("Kas soovite ise võileiva teha(ise), või soovite lasta arvutil teha(arvuti) ? :").lower()
            if kokk == "ise":
                tyyp = input("Kas soovite ühepoolset(1) või kahepoolset(2) võileiba? :")
                m22ris = input("Kas soovite võid(1) või majoneesi(2) ? :")
                l1 = input("Kas soovite kurki? jah/ei :").lower()
                l2 = input("Kas soovite tomatit? jah/ei :").lower()
                l3 = input("Kas soovite peekonit? jah/ei :").lower()
                
                if tyyp == "2":
                    print(sai)
                if l1.lower == "jah":
                    print(kurk)
                    hind += 0.75
                if l2.lower == "jah":
                    print(tomat)
                    hind += 0.75
                if l3.lower == "jah":
                    print(bacon)
                    hind += 0.75
                hind += 0.75 #või/majonees
                print(sai)
                break
            if kokk == "arvuti":
                for i in range(5):
                    i+=1
                    valik = choice([kurk, tomat, bacon])
                    hind += 0.75
                    print(valik)
                print(sai)
                break
            else:
                print("Väär sisend!")
        while True:
            makse = input("Palun makske "+str(hind)+" Eurot. jah/ei :").lower()
            if makse == "jah":
                print("Aitäh tellimuse eest, tulge jälle!")
                break
            elif makse == "ei":
                print("Ootame teid jälle, kui on isu ja raha.")
                break
            else:
                print("Väär sisend!")
        break
    elif isu == "ei" or isu == "":
        print("Ootame teid, kui isu on!")
        break
    else:
        print("Väär sisend!")