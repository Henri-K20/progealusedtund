fail = open("Andmed\joostud.txt", encoding="UTF-8")
# for rida in fail:
#     if float(rida) > 10:
#         print(float(rida))
# fail.close()
kokku = []
keskmine = 0
for rida in fail:
    kokku.append(float(rida.strip()))
fail.close()
print("Siin on kõik tulemused kokku:\n", sum(kokku))

print("\nSiin on tulemused, mis on 10km või alla:")
for arv in kokku:
    keskmine += arv
    if arv <= 10:
        print(arv)
print(f"\nJooksude keskmine on: {round(keskmine/len(kokku),2)} km")