mystring = "Bla Bla bla"

name = "LisSA Simpson"

print(name.title())
print(name.upper())
print(name.lower())

print("Hi str 1\nHi str 2\n\nHi str 3")
print("Message:\n\tMessage1\n\tMessage2\n\tMessage3\nEND")

mixstr = " . some str . "
print("mixstr: " +  mixstr)
print("mixstr.rstrip: " + mixstr.rstrip())
print("mixstr.lstrip: " + mixstr.lstrip())
print("mixstr.strip: " + mixstr.strip())

b = mixstr.strip() #Del spases
b = b.strip(".")   #Del dots
b = b.strip()      #Del spases again
print(b)