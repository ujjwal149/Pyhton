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



#Initilize Dictionaries

# store data in key:value pair by the help of key we can access value.
student_score = {'Harry':29,'Jack':30,'Jordan':21,'Adwin':28,}
print(student_score['Jordan'])

#we can pass new data inside dictionaries
student_score['Natasha']=30
print(student_score)
#we can manipulate data inside dictionaries
student_score['Harry']=30
print(student_score)
#we can remove all data from dictionaries
# student_score = {}
# print(student_score)

#loop inside dictionaries
for i in student_score:
    print(i)
    print(student_score[i])

