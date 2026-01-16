#Dictionaries data type.....
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

