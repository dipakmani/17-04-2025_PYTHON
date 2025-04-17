
# Decision making in Python

# Sometimes, python programs has to take decisions using certain conditions

# 1) The number is even or odd
# 2) Voting Age


# # IF STATMENTS

# If statements is used for decision making.
# In if, we check a condition. depending on truth value of condition, decision will be taken.
# Written using 'if' keyword

# Syntax:-
#             if condition/test_expression:
#                     statement 1
#                     statement 2
                # rest of statements

# if True:
#     print("This is True")


# if True:
#     print("This is True")
#     print("This is proved")

# if True:
#     print("This is True")
#     print("This is proved")
# print("my name is dipak")


# if False:
#     print("This is True")


# if False:
#     print("This is True")
#     print("This is proved")
# print("my name is dipak")

# Python program for even number

# num = int(input("Enter a number:"))
# if num % 2 == 0: # condition
#     print("This is a even number")
# else:
#     print("Odd Number")


# Haam single mai bhi print likh sakte hai

# num = int(input("Enter a number:"))
# if num % 2 == 0: print("This is a even number")


# if 3 < 4:
#     print("3 is less than 4")
#     print("ok")
# print("regular code")

# if 3 > 4:
#     print("3 is less than 4")
#     print("ok")
# print("regular code")

# if 3 < 4 and 4 < 5:
#     print("3 is less than 4")
#     print("ok")
# print("regular code")

# if 1:
#     print("3 is less than 4")
#     print("ok")
# print("regular code")

# if 0:
#     print("3 is less than 4")
#     print("ok")
# print("regular code")

# if None:
#     print("3 is less than 4")
#     print("ok")
# print("regular code")


# if True:
#     print("3 is less than 4")
#      print("ok")          # IndentationError: unexpected indent
# print("regular code")

# # 1. Check if a number is positive

# num = 10
# if num > 11:
#     print("Positive Number")

# # 2. Check if a string is empty

# text = ""
# if not text:
#     print("The string is empty")

# # 3. Check if a list has elements

# my_list = [1, 2, 3]
# if my_list:
#     print("List is not empty")

# # 4. Check if a key exists in a dictionary
# my_dict = {"a": 1, "b": 2}
# if "a" in my_dict:
#     print("Key exists")


# # 5. Check if a number is even
# num = 4
# if num % 2 == 0:
#     print("Even number")

# # 6. Check if a person can vote
# age = 20
# if age >= 18:
#     print("Eligible to vote")

# # 7. Check if a string contains a character
# word = "Python"
# if "y" in word:
#     print("Contains 'y'")

# # 8. Check if a number is a multiple of 5
# num = 25
# if num % 5 == 0:
#     print("Multiple of 5")

# # 9. Check if a number is greater than another number
# a, b = 10, 5
# if a > b:
#     print("a is greater than b")

# # 10. Check if a string starts with a specific letter
# name = "Alice"
# if name.startswith("A"):
#     print("Starts with A")

# # 11. Check if a user is authenticated
# user_authenticated = True
# if user_authenticated:
#     print("Access granted")

# # 12. Check if a list contains a specific value
# values = [10, 20, 30]
# if 20 in values:
#     print("Value found")

# # 13
# energy = "Solar"
# if energy in ["Solar", "Wind", "Hydro"]:
#     print(f"{energy} is a renewable energy source")

# # 14
# animal = "Chameleon"
# if animal in ["Chameleon", "Octopus", "Leaf-tailed Gecko"]:
#     print(f"{animal} can camouflage")

# # 15
# temperature = 42  # in Celsius
# if temperature > 43:
#     print("Heatwave Alert!")

# # 16
# endangered_animals = ["Panda", "Tiger", "Rhino"]
# animal = "Tiger"
# if animal in endangered_animals:
#     print(f"{animal} is endangered")

# # 17
# runs = 105
# if runs >= 100:
#     print("Century scored!")

# # 18
# team1_score = 250
# team2_score = 250
# if team1_score == team2_score:
#     print("Match is a draw")

# # 19
# rain = True
# if rain:
#     print("Match delayed due to rain")

# # 20
# fire_intensity = "High"
# if fire_intensity == "High":
#     print("Evacuate immediately!")

# # 21
# occupied_beds = 250
# total_beds = 300
# if occupied_beds / total_beds > 0.9:
#     print("Hospital is near full capacity")

# # 22
# age = 20
# if age > 18:
#     if age < 30:
#         print("Young adult")

# # 23
# age = 20
# if age >= 18 and age <= 60:
#     print("Eligible for job")

# # 24

# x = 12
# if x > 0:
#     print("positive number")
# if x % 2 == 0:
#     print("Even number")
# if x > 10:
#     print("Greater than 10")


