"""Function"""
def my_function():
    print("hello world")

my_function()

"""Greeting Function"""

def greeting (name):

    print(f"Hello {name}")

name = "Ujjwal"
greeting(name)

#more than one parameter
def greetings(nam,location):
    print(f"Hello {nam}")
    print(f"Hope you are doing well in {location}")

greetings("virat","uk")

#Positional Arguments
def calculator(a,b,c):
    print(a+b+c)

calculator(1,4, 8)

#keyword Argument
def calculator(d,e,f):
    print(d+e+f)

calculator(d=1,f=4, e=8)
