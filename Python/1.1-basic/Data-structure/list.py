import random
'''Python provides versatile data structures
 like lists, tuples, and dictionaries to store and manipulate data efficiently.
  Below are examples and explanations for each:'''

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

#Nested List
nested_list = ['A','B',['C','D']]
#print D
print(nested_list[2][1])