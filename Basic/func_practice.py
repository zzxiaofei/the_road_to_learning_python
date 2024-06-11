import flask


def func_practice(username):
    print(f"Hello,{username.title()}")


def display_message():
    print('function')


def favorite_book(bookname):
    print("I love " + bookname)


def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s nam is {pet_name.title()}")


func_practice('Daniel')
display_message()
favorite_book('Alice in Wonderland')
describe_pet('hamster', 'harry')
describe_pet('dog','dudu')
