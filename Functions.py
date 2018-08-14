def print_greetings(name):
    """Prints greeting Words"""
    print(name.title() + ", hello!")


def sumNumbs(x, y):
    """sums numbers"""
    return int(x) + int(y)


def factorial(x):
    """Calculate factorial of the number X"""
    result = 1
    for i in range(1, x + 1):
        result*= i
    return result


print_greetings("vasia")
print(sumNumbs(2, 5))
print(factorial(3))

for i in range(1, 5):
    print(str(i) + '! = ' + str(factorial(i)))

print('==================================')

def create_record(name, phone, adress):
    """Creates a record with name, phone and adress"""
    record = {
        "name": name.title(),
        "phone": phone,
        "adress": adress
    }
    return record


user1 = create_record("Vasia", '000', 'Ukraine')
user2 = create_record("Petia", '111', 'Poland')

print(user1)
print(user2)

def give_avard(medal, *persons):
    """Gives medal to persons"""
    for person in persons:
        print(person['name'] + " avarded with medal " + medal)


give_avard("For the courage", user1, user2)
give_avard("For the blue eyes", user1)