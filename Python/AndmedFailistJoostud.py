fail = open("Andmed\joostud.txt", encoding="UTF-8")
# for rida in fail:
#     if float(rida) > 10:
#         print(float(rida))
# fail.close()
kokku = []
keskmine = 0
for rida in fail:
    kokku.append(rida)
fail.close()
print("Siin on kõik tulemused:\n", *kokku)
print("Siin on tulemused, mis on 10km või alla:")
for arv in kokku:
    keskmine+=float(arv)
    if float(arv) <= 10:
        print(arv.strip())
print(f"\nJooksude keskmine on: {round(float(arv)/len(kokku),2)} km")