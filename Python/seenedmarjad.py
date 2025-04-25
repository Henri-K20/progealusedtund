seened = ["pilvik", "kukeseen", "mürklid", "puravik", "võiseen"]
marjad = ["mustikas", "jõhvikas", "vaarikas", "karusmari", "must sõstar"]
midaOtsib = ""

while midaOtsib == "":
    midaOtsib = input("Kas te otsite seent või marja?\n:").lower()

if midaOtsib == "seent":
    print("""########################
Sisestage valiku number.""")
    for seen in seened:
        print(f"""
{seened.index(seen)}: {seen.capitalize()}
""",end="")
    midaOtsib = input("\n->")
    match midaOtsib:
        case 0:
            
        case 1:
            
        case 2:
            
    
    
#elif midaOtsib == "marja":
    
