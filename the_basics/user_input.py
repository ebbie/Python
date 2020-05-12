# def weather_condition(temperature):
#     if temperature > 7:
#         return "Warm"
#     else:
#         return "Cold"

# user_input = float(input("Enter temperature:"))
# print(weather_condition(user_input))

name = input("Enter your name: ")
surname = input("Enter your surname: ")
# message = "Hello %s %s" % (name, surname)
# message = "Hello %s!" % user_input --- This works in both Python 2 and Python 3
# message = f"Hello {user_input}!" # This only works in Python 3.6 or higher version
message = f"Hello {name} {surname}"
print(message)


