# What is a List in Python?
# 1. A list in Python is a mutable, ordered collection that allows you to store multiple 
# values of different data types. Lists are created using square brackets [ ],
# and elements inside a list are separated by commas.

# Why Use Lists?
# Ordered: Items in a list retain their sequence.

# Mutable: Lists can be modified (add, remove, update elements).

# Heterogeneous: Can store different data types (integers, strings, etc.).

# Dynamic: Lists can grow and shrink as needed.

# Use Case of Lists
# Lists are commonly used when you need to store, retrieve, and modify
# a collection of items dynamically.
# For example, in an e-commerce website, a list can be used to store the 
# shopping cart items of a user.

# shopping_cart = ["Laptop", "Mouse", "Keyboard", "USB Cable"]
# print(shopping_cart)

# 1. Create a List and Print It

# fruits = ["Apple", "Banana", "Cherry"]
# print(fruits)

# 2. Access an Element by Index

# numbers = [10, 20, 30, 40, 50, 60]
# print(numbers[2])

# 3. Negative Indexing

# languages = ["Power BI", "Python", "Java", "React Js", "TABLEAU"]
# print(languages[-2])

# 4. Slicing a List

# colors = ["Red", "Green", "Blue", "Yellow", "Purple"]
# print(colors[:])

# print ("--------------------------------------------")
# colors = ["Red", "Green", "Blue", "Yellow", "Purple"]
# print(colors[:4])


# print ("--------------------------------------------") 

# colors = ["Red", "Green", "Blue", "Yellow", "Purple"]
# print(colors[0:0])

# print ("--------------------------------------------") 

# colors = ["Red", "Green", "Blue", "Yellow", "Purple"]
# print(colors[1:4])

# # 5. Append an Element

# numbers = [1, 2, 3]
# numbers.append(4)
# print(numbers)

# print ("--------------------------------------------") 


# num = [10,20,30,40]

# num.append(50,60)  # ERROR
# print(num)

# 6. Insert an Element at a Specific Position and append and insert we can add at a time

# numbers = [1, 3, 4]
# numbers.insert(1, 2)
# print(numbers)

print ("--------------------------------------------") 

# numbers = [1, 3, 4]
# numbers.insert(1, 2)
# numbers.append(6)
# print(numbers)

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# list1.extend(list2)
# print(list1)

# 8. Remove an Element

# fruits = ["Apple", "Banana", "Cherry"]
# fruits.remove("Banana")
# print(fruits)

# fruits = ["Apple", "Banana", "Cherry"]  # WILL GET ERROR BECAUSE WE CAN'T REMOVE USING INT
# fruits.remove("1")
# print(fruits)

# list = [10, 20, 30, 40, 50]
# print(list)

# print(dir(list))

# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__',
# '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
# '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', 
# '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', 
# '__reduce_ex__', '__repr__',
# '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', 
# '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 
# 'pop', 'remove', 'reverse', 'sort']

# List Comprehension
# 1. 

# marks = [20, 30, 40, 50, 60]
# new_marks = [ ]
# for i in marks:
#     new_marks.append(i+2)
#     new_marks.append(i+4)
# print(new_marks)

# print("--------------------------------------------")

# Using Comprehension

# marks = [20, 30, 40, 50, 60]
# new_marks = [x+2 for x in marks]
# print(new_marks)

# print("--------------------------------------------")

# 2
# cubes = []
# for i in range(10):
#     if i % 2 == 0:
#         cubes.append(i ** 3)
# print("Using for loop:", cubes)

# print("--------------------------------------------")

# Using List Comprehension 

# easy = [i ** 3 for i in range(10) if i % 2 == 0]
# print("Using list comprehension:", easy)

# print("--------------------------------------------")
# 3

# lst = []
# for i in range(100):
#     if i % 3 == 0:
#         lst.append(i)
# print(lst)

# Using Comprehension

# ls = [i for i in range(100) if i % 3 == 0]
# print(ls)

# 4  Converting Strings to Uppercase

# words = ["apple", "banana", "cherry"]
# upper_words = []
# for word in words:
#     upper_words.append(word.upper())
# print(upper_words)


upper_words = [word.upper() for word in ["apple", "banana", "cherry"]]
print(upper_words)



# dict comprehension

# dict1 = {i: f"item {i}" for i in range(101) if i % 10 == 0}
# print(dict1)

# dict1 = {i: f"Item {i}" for i in range(5)}
# dict2 = {value:key for key,value in dict1.items()}
# print(dict1, dict2)

# dresses = {dress for dress in ["dress1", "dress2", "dress1", "dress2", "dress2"]}
# print(type(dresses))
# print("---------------------------------------------")
# print(dresses)

 