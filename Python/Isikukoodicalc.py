from random import *
vanus = 0
bday = 0
bmonth = 0
byear = ""
sugu = ""
i = True
idkood = ""
while i:
    try:   
        vanus = int(input("Sisestage oma vanus.\n:"))
        bday = int(input("Sisestage oma sünnipäev. \n:"))
        bmonth = int(input("Sisestage oma sünnikuu. (Kuu number) \n:"))
        byear = input("Sisestage oma sünniaasta. (Viimased kaks numbrit)\n:")
        sugu = input("Sisestage oma sugu. m/n \n:").lower()
    except ValueError:
        input("Väär andmetüüp! Sisestage ainult arve. Vajutage enter, et uuesti proovida.")
    else:
        i = False
        break
if i == False:
    if sugu == "m":
        sugu = choice([3,5])
    else:
        sugu = choice([4,6])
    if len(str(bmonth)) == 1:
        bmonth = "0" + str(bmonth)
    idkood = str(sugu)+str(byear)+str(bmonth)+str(bday)+str(randint(1000,9999))
    nimi = input("Sisestage oma ees- ja perekonnanimi.\n:").title()
    print(f"Palun, {nimi} siin on teie isikukood.\n{idkood}")