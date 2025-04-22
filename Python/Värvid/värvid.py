fail = open("colors.txt",encoding="UTF-8")
read = []
i = 0
for rida in fail:
    if i % 8 == 0 or i == 0:    
        read.append(rida.strip("\n"))
    i+=1
fail.close()
print(read)