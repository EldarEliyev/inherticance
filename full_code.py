# 1.python tutorial for beginners: PYTHON FULL COURSE FOR FREE(Bro code)
# print("I like pizza!")
# print("It's really good!")

#2.variable
# first_name = "Eldar"
# last_name = "Eliyev"
# full_name = first_name + last_name
# print("Hello "+  full_name)
# # print(type(name))

# age = 19
# age = age + 1
# print(age)
# print(type(age))


# height = 250.5
# print("Your height is: " +str(height)+"cm")
# print(type(height))


# human = True
# print("Are you a human:" +str(human))
# print(type(human))

# name = "bro"
# age = 21
# attractive = True
# print(name)
# print(age)
# print(attractive)

# Spongebob = 30
# Patrick = 30
# Sandy = 30
# Squidward = 30

# print(Spongebob)
# print(Patrick)
# print(Sandy)
# print(Squidward)



#String methods
# name = "Eldar"
# print(len(name))
# print(name.find("a"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count("a"))
# print(name.replace("a", "o"))
# print(name*3)



# x = 1
# y = 2.0
# z = "3"

# x = str(x)
# y = str(y)
# z = str(z)

# print(x)
# print(y)
# print(z*3)



#User Input:
# name = input("What is your name?")
# age = int(input("How old are you?"))
# height = float(input("How tall are you?"))

# print("Hello" + name)
# print("You are" +str(age)+"years old")
# print("You are"+str(height)+"cm tall")



#7.Math functions
# import math
# pi = 3.14
# x = 1
# y = 2
# z = 3
# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(pi))
# print(pow(pi,2))
# print(math.sqrt(420))
# print(max(x,y,z))



#8.string slicing
# name = "Eldar code"
# first_name = name[0:3]
# last_name = name[4:8]
# funky_name = name[::3]
# reversed_name = name[::-1]
# print(reversed_name)
# website1 = "http://google.com"
# website2 = "http://wikipedia.com"
# slice = slice(7, -4)
# print(website1[slice])
# print(website2[slice])



# If statement:
# age = int(input("How old are You?"))
# if age == 100:
#     print("You are a centurty old:")
# elif age>=18:
#     print("You are an adult!")
# elif age <0:
#     print("You haven't been born yet! ")
# else:
#     print("You are a child!")



#Logical Operators:
# temp = int(input("What is the temperature outside?"))
# if temp >=0 and temp <=30:
#     print("The temperature is good today!")
#     print("go outside!")
# elif temp <0 or temp >30:
#     print("The temperature is bad today!")
#     print("stay inside!")



# 11.While loops:
# while 1==1:
#     print("Help! I'm stuck in a loop!")

# name = ""
# while len(name) == 0:
#     name = input("Enter your name:")

# print("Hello" + name)





#12.for loops
# import time
# for i in range(10):
#     print(i + 1)
    
#     for i in range(50, 100+ 1,2):
#         print(i)
        
#         for i in "Eldar eliyev":
#             print(i)
            

# for seconds in range(10,0, -1):
#     print(seconds)
#     time.sleep(1)
    
# print("Happy")



# 13.nested loops:
# rows = int(input("How many rows?:"))
# columns = int(input("How many colums?:"))
# symbol = input("Enter a symbol to use: ")

# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")
#         print()



#14.loop control statements : break, continue, pass
# while True:
#     name = input("Enter your name:")
#     if name != "":
#         break
    
# phone_number = "994-70-512-50-75"
# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")



# for i in range(1,21):
#     if i == 13:
#         pass
#     else:
#         print(i)




#15.Lists
# food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]
# food [0] = "sushi"
# food.append("ice cream")
# food.remove("hotdog")
# food.pop()
# food.insert(0, "cake")
# food.sort()
# food.clear()
# for x in food:
#     print(food)




#16.2D lists
# drinks = ["coffee", "soda", "tea"]
# dinner = ["pizza", "hamburger", "hotdog"]
# dessert = ["cake", "ice cream"]
# food = [drinks, dinner, dessert]
# print(food)




#17.Tuple
# student = ("Eldar", 19, "male")
# print(student.count("Eldar"))
# print(student.index("male"))

# for x in student:
#     print(x)
    
# if "Eldar" in student:
#     print("Eldar is here!")




#18.Set
# utensils = {"fork", "spoon", "knife"}
# dishes = {"bowl", "plate", "cup", "knife"}
# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# utensils.update(utensils)
# dinner_table = utensils.union(dishes)
# print(dishes.difference(dishes))
# for x in dinner_table:
#     print(x)


#19.dictionaries
# capitals = {'Usa': 'Washington DC',
#             'India': 'New Dehli',
#             'Russia': 'Moscow',
#             'China': 'Beijing'}

# capitals.update({'Germany':'Berlin'})
# capitals.update({'Usa': 'Las Vegas'})
# capitals.pop('China')
# capitals.clear()
# # print(capitals.keys())
# # print(capitals.values())
# # print(capitals.items())

# for key, value in capitals.items():
#     print(key,value)





#20.indexing:
# name = "Eldar Code!"
# if (name[0].islower()):
#     name = name.capitalize()
    
# first_name = name[:3].upper()
# last_name = name[4:].lower()
# last_character = name[-1]
# print(first_name)
# print(last_name)
# print(last_character)




#21.Functions
# def hello(first_name, last_name, age):
#     print("hello" + first_name+ ""+last_name)
#     print("You are" +str(age)+ "years old")
#     print("Have a nice day!")

# hello("Eldar", "Eliyev", 21)


#22.return statement
# def multiply(number1, number2):
#     return number1 * number2

# x = multiply(6,8)
# print(x)



#23.Keyword arguments
# def hello(first, middle, last):
#     print("Hello "+first, " "+middle+ " "+last)
    
# hello(last="Eliyev", middle="Dude", first="Eldar")



#24.Nested functions calls
# num = input("Enter a whole positive number:")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)
# print(round(abs(float(input("Enter a whole positive number:")))))



#25.Variable Scope
# name = "Eldar"
# def display_name():
#     name = "Eliyev"
#     print(name)
    
# display_name()
# print(name)



#26.args
# def add (*stuff):
#     sum = 0
#     stuff = list(stuff)
    
#     for i in stuff:
#         sum += i
#         return sum
    
# print(add(1,2,3,4,5,6,7,8))



#27.Kwargs
# def hello(**kwargs):
#     print("Hello"  + kwargs['first'] + " " + kwargs['last'])
#     print("Hello", end=" ")
#     for key,value in kwargs.items():
#         print(value, end=" ")
        
# hello(title="Mr", first="Bro", middle="Dude", last="Eliyev")



#28.string format
# number = 1000
# print("The number pi is {:.3f}".format(number))
# print("The number is {:,}".format(number))
# print("The number is {:b}".format(number))
# print('The number is {:o}'.format(number))
# print("The number is {:X}".format(number))
# print("The number is {:E}".format(number))



#29.Random Numbers
# import random
# x = random.randint(1,6)
# y = random.random()
# myList = ['rock', 'paper', 'scissors']
# z = random.choice(myList)
# cards = [1,2,3,4,5,6,7,8,9,"J", "Q", "K", "A"]
# random.shuffle(cards)
# print(cards)


#30.exception handling
# try:
#     numerator = int(input("Enter a number to divide: "))
#     denominator = int(input("Enter a number to divide by: "))
#     result = numerator/ denominator
# except ZeroDivisionError as e:
#     print(e)
#     print("You can't divide by zero! idiot!")
# except ValueError as e:
#     print(e)
#     print("Enter only numbers plz")
# except Exception as e:
#     print(e)
#     print("something went wrong :(")
# else:
#     print(result)
# finally:
#     print("This will always execute")



# #31.file detection
# import os
# path = "C:\\Users\\ELDAR\OneDrive\\Documents\\test.txt"
# if os.path.exists(path):
#     print("That location exists!")
#     if os.path.isfile(path):
#         print("That is a file")
#     elif os.path.isdir(path):
#         print("That is a directory!")
# else:
#     print("That location doesn't exist!")



#32.read a file
# try:
#     with open('test.txt') as file:
#         print(file.read())
# except FileNotFoundError:
#     print("That file was not found:")



#33.Write a file:
# text = "Yoooooooooooo\nThis is some text\nHave a good one!\n"
# with open('test.txt', 'w') as file:
#     file.write(text)


#34.copy a file:
# text = 'Have a nice today! see ya'
# with open('test.txt', 'a') as file:
#     file.write(text)


#36.delete a file
# import os
# import shutil
# path = "test.txt.txt"
# try:
#     os.remove(path)
#     os.rmdir(path)
#     shutil.rmtree(path)
# except FileNotFoundError:
#     print("That file was not found")
# except PermissionError:
#     print("You do not have permission to delete that")
# except OSError:
#     print("That folder contains files")
# else:
#     print(path+" was deleted")



#38.rock,paper,scissors game
# import random
# while True:
#     choices = ["rock", "paper", "scissors"]
#     computer = random.choice(choices)
#     player = None
    
#     while player not in choices:
#         player = input("rock, paper, or scissors?:").lower()
        
#         if player == computer:
#             print("computer:", computer)
#             print("player:",player)
#             print("Tie!")
            
            
#         elif player == "rock":
#             if computer == "paper":
#                 print("computer", computer)
#                 print("player:", player)
#                 print("You lose!")
                
#                 if computer == "scissors":
#                     print("computer:", computer)
#                     print("player:", player)
#                     print("You win!")
                    
#                 elif player == "paper":
#                     if computer == "scissors":
#                         print("computer:", computer)
#                         print("player:", player)
#                         print("You lose!")
                        
#                         if computer == "rock":
#                             print("computer:", computer)
#                             print("player:", player)
#                             print("You win!")
                
#             play_again = input("Play again? (yes/no):").lower()
            
#             if play_again != "yes":
#                 break
#             print(" Bye!")
            




#40.OBJECT ORIENTED PROGRAMMING (OOP)
from car import Car
