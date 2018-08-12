x = 25
if x == 25:
    print("YES")
else:
    print("NO")

age = 13
if age <= 4:
    print("You are baby")
elif age >4 and age <=12:
    print("You are tkid")
elif age >12 and age <=18:
    print("You are teenager")
else:
    print('You are old')

print("=====END=====")

cities = ['Kiev', 'Dnipro', 'London', 'Glasgo', 'Tirol', 'Krakow', 'Minsk']
capitals = ['Kiev', 'London', 'Minsk']

if 'Kiev' in cities:
    print("yes, Kiev is in the list")
else:
    print("No")

for city in cities:
    if city in capitals:
        print(city + ' is a capital')
    else:
        print(city + ' is not a capital')