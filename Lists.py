names = ['Homer', 'Lisa', 'meggy', 'Bart', 'Marge']
print(len(names))
print(names[0])
print(names[-1])
print(names[2].title())

names[2] = names[2].title()
names.append('Santa\'s Little Helper')
names.insert(2, 'Snowball')
names.insert(2, 'Snowball II')
names.insert(2, 'Snowball III')
print(names)

del names[2]
print(names)

names.remove('Snowball II')
print(names)

deleted_name = names.pop()
print(deleted_name)
print(names)

names.sort()
print(names)

names.reverse()
print(names)

for name in names:
    print(name.upper())

for x in range(0, len(names)):
    print(str(x) + ': ' + names[x])

number_list = list(range(0, 10))
print(number_list)

print(max(number_list))
print(min(number_list))
print(sum(number_list))

mynames = names[1:3]
print(mynames)
print(names[:-1])
print(names[-2:])

my_new_names_1 = names
my_new_names_2 = names[:]
names.append('some new name')
print(my_new_names_1)
print(my_new_names_2)