def liida(x,y):
    return x + y
def lahuta(x,y):
    return x - y
def korruta(x,y):
    return x * y
def jaga(x,y):
    return x / y
def astenda(x,y):
    return x ** y
vaste = "x"

while vaste != "":
    vaste = input("""
#####################
Sisestage valiku arv!
0. liida
1. lahuta
2. korruta
3. jaga
4. astenda
Vajutage enterit, et lahkuda!
#############################
:""")
    if vaste != "":
        x = int(input("Sisesta esimene arv!\n:"))
        y = int(input("Sisesta teine arv!\n:"))

        match vaste:
            case "0":
                vaste = liida(x,y)
            case "1":
                vaste = lahuta(x,y)
            case "2":
                vaste = korruta(x,y)
            case "3":
                vaste = jaga(x,y)
            case "4":
                vaste = astenda(x,y)
        print(f"Teie tehe vastust on: {vaste}!\n")
    else:
        print("Head aega!")
