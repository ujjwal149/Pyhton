
import random


friends_list = ["Alice","Bob","Charlie","David"]

#option.1
random_index =(random.randint(0,3))
print (friends_list[random_index])
#option.2
print(random.choice(friends_list))

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1])