inputfile = "files/names.txt"

myFile = open(inputfile, mode='r', encoding="ascii")

for index, line in enumerate (myFile, 1):
    if "Genevieve" in line:
        print("Line N " + str(index) + " " + line.strip())

myFile.close()

print('==================================')

str_to_look_for = "koli"
inputBigFile = "files/big-file.txt"
outputVasilFile = "files/vasilPasswords.txt"

myBigFile1 = open(inputBigFile, mode='r', encoding="latin_1")
myBigFile2 = open(outputVasilFile, mode='a', encoding="latin_1")

for index, line in enumerate (myBigFile1, 1):
    if str_to_look_for in line:
        print("Line N " + str(index) + " " + line.strip())
        myBigFile2.write("found password: " + line)

myBigFile1.close()
myBigFile2.close()
