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
student_score = {}
print(student_score)

#loop inside dictionaries
for i in student_score:
    print(i)
    print(student_score[i])



#Nested list in dictionaries.
travel_log = {
    'French':['Paris','Lille','Dijon'],
    'Germany':['Stuttgart','Berlin'],
}
print(travel_log['French'])
print(travel_log['French'][1])

#Nested list and dictionaries inside dictionaries

travel_log = {
    'French':{
        'cities-visited':['Paris','Lille','Dijon'],
        'Time-visited':3,
    },
    'Germany':{
        'cities-visited':['Stuttgart','Berlin'],
        'Time-visited':5
    }
}
print(travel_log['French']['cities-visited'][2])
print(travel_log['French']['Time-visited'])