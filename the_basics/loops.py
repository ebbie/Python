# monday_temperatures = [9.1, 8.8, 7.6]

# for temperature in monday_temperatures:
#     print(round(temperature))

# for letter in 'hello':
#     print(letter)

# looping through a dictionary
student_grades = {"Mary": 9.1, "Sam": 8.8, "John": 7.5}

for grades in student_grades.items():
    print(grades)

for grades in student_grades.values():
    print(grades)

for grades in student_grades.keys():
    print(grades)

for grades in student_grades.items():
    print("{}'s grade is {}".format(grades[0], grades[1]))


