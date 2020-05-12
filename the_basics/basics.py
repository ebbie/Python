""" import datetime
print("The date and time is: ", datetime.datetime.now())

student_grades = [9.1, 8.8, 7.5]
student_namesWithGrades = {"Mary": 9.1, "Sam": 8.8, "John": 7.5}
print(student_namesWithGrades)
print(student_namesWithGrades.keys())
print(student_namesWithGrades.values())

print(student_grades)
print(max(student_grades))
mysum = sum(student_grades)
length = len(student_grades)
mean = mysum / length
print("Mean: ", mean)

list1 = list(range(1, 10))
print(list1)

list2 = list(range(1,10,3))
print(list2)
 """
#A tuple is just like a list but wiht paranthesis
# Tuples are immutable and lists are mutable which means in list we can add more items to the list adn append items
monday_temperatures = (1,4,5)
print(monday_temperatures)

monday_temperatures2 = [1,4,5]
monday_temperatures2.append(6)
print(monday_temperatures2)
