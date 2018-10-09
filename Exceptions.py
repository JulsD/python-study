
import sys
inputfile = "files/name.txt"

while True:
    try:
        print("inside TRY")
        myFile = open(inputfile, mode='r', encoding="ascii")
    except Exception:
        print("inside EXCEPTION")
        print("error found")
        print(sys.exc_info()[1])
        inputfile = input("Please enter correct file name: ")
    else:
        print("inside ELSE")
        print(myFile.read())
        sys.exit()
    finally:
        print("inside FINALLY")



print("=========END========")