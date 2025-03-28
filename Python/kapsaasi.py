while True:
    hapukapsas = input("Kas teil on hapukapsas? jah/ei\n:").lower()
    if hapukapsas == "ei":
        hapukapsas = False
    elif hapukapsas == "jah":
        hapukapsas = True
    pott = input("Kas teil on pott? jah/ei\n:").lower()
    if pott == "ei":
        pott = False
    elif pott == "jah":
        pott = True
    vett = input("Kas teil on vett? jah/ei\n:").lower()
    if vett == "ei":
        vett = False
    if vett == "jah":
        vett = True
    kartul = input("Kas teil on kartulit? jah/ei\n:").lower()
    if kartul == "ei":
        kartul = False
    if kartul == "jah":
        kartul = True
    puljong = input("Kas teil on puljongit? jah/ei\n:").lower()
    if puljong == "ei":
        puljong = False
    if puljong == "jah":
        puljong = True
    muud = input("Kas teil on veel midagi kapis? jah/ei\n:").lower()
    if muud == "ei":
        muud = False
    if muud == "jah":
        muud = True
    
    if (pott and  muud) and (hapukapsas and kartul and puljong):
        print("Saate teha ühepajatoitu!")
    if (pott and not vesi and not muud) and (hapukapsas and kartul and puljong):
        print("Saab teha mulgikapsaid!")
    if (not pott) and ( hapkapsas and  kartul and  puljong and  muud and vett):
        print("Ei saa teha mitte midagi!")
    if (not hapukapsas and not muud) and pott and vett and puljong and kartul:
        print("Saab teha hautist!")
    if (pott and not vesi and not muud) and (hapukapsas and kartul and puljong):
        
    
    