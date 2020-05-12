# def mean(mylist):
#     the_mean = sum(mylist) / len(mylist)
#     return the_mean

# print(mean([1,4,5]))

# print(type(mean), type(sum))

### Using Conditionals
def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean

monday_temperatures = [9.1, 8.8, 7.5]
student_namesWithGrades = {"Mary": 9.1, "Sam": 8.8, "John": 7.5}
print(mean(monday_temperatures))
print(mean(student_namesWithGrades))