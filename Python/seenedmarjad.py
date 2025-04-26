seened = ["pilvik", "kukeseen", "mürklid", "puravik", "võiseen"]
marjad = ["mustikas", "jõhvikas", "vaarikas", "karusmari", "must sõstar"]
midaOtsib = ""

while midaOtsib == "":
    midaOtsib = input("Kas te otsite seent või marja?\n->").lower()

if midaOtsib == "seent":
     while midaOtsib not in seened: 
        print("""########################
Sisestage valiku number.""")
        for index, seen in enumerate(seened):
            print(f"{index}: {seen.capitalize()}")
        
        try:
            midaOtsib = seened[int(input("\n->"))]
        except (IndexError, ValueError):
            input("Väär sisestus! Vajuta enterit, et uuesti proovida!\n->")
        else:
            print(midaOtsib)
#     match midaOtsib:
#         case 0:
#             
#         case 1:
#             
#         case 2:
#             
#         case 3:
#             
#         case 4:
#             
#         case 5:
#             
#         case _:
#             print("oiei!")



#elif midaOtsib == "marja":

