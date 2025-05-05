from urllib.request import urlopen
from webbrowser import *

fail = urlopen("https://jurivaitmaa21.thkit.ee/ahtt6.txt")
baidid = fail.read()
tekst = baidid.decode()
tekstrida = tekst.splitlines()
fail.close()

tõde = 0
õigus = 0

for rida in tekstrida:
    sõnad = rida.split()
    for s in sõnad:
        if s.strip(".,?") == "tõde":
            tõde+=1
        if s.strip(".,?") == "õigus":
            õigus+=1

print(f"Tõde: {tõde}, Õigus: {õigus}")

print(tekstrida)