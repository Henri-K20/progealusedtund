fail = open("colors.txt",encoding="UTF-8")
read = []
read1 = []
for rida in fail:
    read.append(rida.strip("\n"))
fail.close()
read1.append(read[0::8])
print(read1)