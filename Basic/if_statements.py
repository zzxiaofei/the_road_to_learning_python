import  random

# .lower() / .upper() / .title()
cars = ['audi', 'bmw', 'subaru', 'benz']
for car in cars:
    if car.lower() == 'audi':
        print(car.upper())
    else:
        print(car.title())

age = 120
if age >=0 or age <=120:
    print("You are")
else:
    print("You are no")

python_score = 60
c_score = 40
if python_score >= 60 or c_score >= 60:
    print("You are")
else:
    print("You are failed")

is_employee = True
if is_employee:
    print('You are our employee')
else:
    print("Please")

has_ticket = True
knife_length = 20
if has_ticket:
    print('You have ticket')
    if knife_length <= 20:
        print('You are allowed')
    else:
        print('You are not allowed')
else:
    print('You have not ticket')


player = int(input('Enter a number: 石头（1）/ 剪刀（2）布（3）'))
computer = 1
print("玩家选择的拳头是 %d - 电脑除的拳是 %d " % (player, computer))

