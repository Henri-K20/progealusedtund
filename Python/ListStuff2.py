tänavad = []
vaste = "1"
halb = 0
täht = ""

while vaste != "":
    vaste = input("Sisesta oma kodukandi tänavanimesi. Kui rohkem ei ole, vajuta enter.\n:").lower()
    if vaste != "":
        tänavad.append(vaste)
    
while täht == "":
    täht = input("Milline täht ei meeldi?\n:").lower()
    if len(täht) > 1:
        print("Sisesta üks täht!")

print("""
###########################
Tänavad, kus ei ole tähte:
""")
for tänav in tänavad:
    if not täht in tänav:
        print(tänav)
    if täht in tänav:
        halb+=1
print("""
###########################
""")
print(f"Täht leidub {halb} tänavas.")