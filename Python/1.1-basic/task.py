# print("1. Mix 500g of Flour, 10g Yeast and 300ml water in a bowl.")
# print("2. Knead the dough for 10 minutes.")
# print("3. Add 3g of Salt.")
# print("4. Leave to rise for 2 hours.")
# print("5. Bake at 200 degrees C for 30 minutes.")


# print("1. Mix 500g of Flour, 10g Yeast and 300ml water in a bowl.\n2. Knead the dough for 10 minutes.\n3. Add 3g of Salt.\n4. Leave to rise for 2 hours.\n5. Bake at 200 degrees C for 30 minutes.")
# print("Hello"+"Ujjwal")
#
# print("Notes for Day 1")
# print("The print statement is used to output strings")
# print("Strings are of characters")
# print("String Concatenation is done with the + sign")
# print("New lines can be created with a \ and the letter n")


# print("Hello"+input("what is your name?") + "!")


"""Variable in Python"""
from scipy.signal.windows import exponential

# name = input("Your name:")
# print("Hello"+name)

"""find the length of the string in python"""

# length = len(name)
# print(length)

"""1st Project
BandName Generator"""
#
# print("BandName Generator")
# cityName = input("Enter your city name: ")
# petName = input("Enter your pen name: ")
#
# print(cityName + petName)

"""Variable in Python"""
#strings
# print("134"+"325")
# print("Hello"[0])
# print ("hello"+"Boy")

#integers
# print(124+253)

#large integers
# print(127395211)
# print(127_395_211) #underscore is for visually understanding large number.

#float = floating point number
# print(3.14159)

#Boolean
# True
# False


"""" len function"""
# print(len("Hello"))

"""Type of Data"""
# print(type(123))
# print(type(1.234))
# print(type("Hello"))
# print(type(True))

# """"TypeCast in Python"""
# int("145")
# int("167")
#
# print(type(int("145")))
# print(int(145)+int(167))
#
# int()
# float()
# str()
# bool()
#
# print("My age is: " + str(12))
#
# print("Your name has : "+ str(len(input("Enter your name: "))) + " letter")
#
# """"Mathematical Operations"""
#
# print(126+351)
# print(7-3)
# print(7*3)
# print(4**2) # double ** find out the exponential
# print(6/3)
# print(6//3) # single / always provide answer  in floating point , to change it integer we use //
#
# """round function"""
# #round(number, ndigits=None)
# bmi = 84/1.65*2
# print(bmi)
# print(round(bmi,3))

"""Assignment Operators"""
# score = 0
# print(score)
#
# score += 1
# print(score)
#
# score -= 1
# print(score)
#
# score *= 2
# print(score)
#
# score /= 2
# print(score)

"""f strings : it allow us to print different data type inside one statement just by adding f in front of starting """
# yourName = "Ujjwal"
# year = 4
# score = 7.2
# isPass = True
#
# print(f"{yourName} a {year}th year cgpa is {score} pass {isPass}")

"""" Split Calculator """
# price = input("Enter the bill amount: ")
# per = input("How much % you want to give tips: ")
# splitInto = input("Total number of person to split b/w: ")
#
# tipsOnly=(int(price)*(int(per)/100))
# totalPrice = int(price) + int(tipsOnly)
# round(totalPrice,2)
# finalPrice = totalPrice/int(splitInto)
# print(f"{finalPrice} rs have to pay per person")


"""Control Flow with if/else and condition"""
#Age checker to get permission to drive car:
# age = 18
# if age >= 18:
#     print("You can drive.")
# else:
#     print("You can't drive.")

#Odd Even tester:
# digit = int(input("Enter a number: "))
# if digit % 2 == 0:
#     print(f"{digit} is a Even number")
# else:
#     print(f"{digit} is a Odd number")


"""Nested if-else Statement"""
# print("Welcome to roller-coaster ride ")
# height = int(input("Enter your height in cm: "))
#
# if height >= 120:
#     print("You can ride")
#     age = int(input("Enter your age: "))
#     if age >= 18:
#         print("Ticket price 250rs")
#     elif age < 18 and age <= 12:
#         print("Your ticket price 100rs")
#     else:
#         print("Ticket price 150rs")
# else:
#     print("You can't ride")

""" Multiple if """

"""Pizza order"""
# print("Welcome to python pizza delivery")
# size = input("Select pizza size S,M,L: ")
# pepperoni = input("Do you want pepperoni on your pizza?(Y/N): ").lower()
# extra_cheese = input("Do you want extra cheese on your pizza?(Y/N): ")
#
# pay = 0
# price_S_pizza = 75
# price_M_pizza = 150
# price_L_pizza = 200
#
# price_pepperoni = 15
# price_extra_cheese = 50
#
# if size == "s":
#     pay=price_S_pizza
#     if pepperoni == "y":
#         pay += price_pepperoni
#
#
# elif size == "m":
#     pay = price_M_pizza
#     if pepperoni == "y":
#         pay += price_pepperoni
#
# elif size == "l":
#     pay = price_L_pizza
#     if pepperoni == "y":
#         pay += price_pepperoni
#
# else:
#     print("Please enter a valid choice")
#
# if extra_cheese == "y":
#     pay += price_extra_cheese
#
# print(f"You total pay {pay}rs")

"""Logical Operators (and,or,not)"""


