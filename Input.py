name = input('Please enter your name: ')
print('Hi ' + name + '!')

num1 = input('Enter X: ')
num2 = input('Enter Y: ')
sumNums =  int(num1) + int(num2)
print(sumNums)

print('==============================')

while True:
    message = input('Enter password: ')
    if message == 'secret':
        break
    print(message + ' password is not correct')

print('==============================')

myList = []
msg = ''
while msg.lower() != 'stop':
    msg = input('Enter new item and stop to finish')
    myList.append(msg)

print(myList)