# # What is a Function?

# # A function is a block of reusable code that performs a specific task.

# # Think of it like a recipe: you give ingredients (inputs), follow some
# #  steps (code), and get a dish (output).

# # ✅ Why use Functions?
# # Avoid repetition (DRY: Don’t Repeat Yourself)

# # Make code modular and readable

# # Easy to test and debug

# # Helps in organizing code better

# def greet():
#     print("Hello")
#     print("Hi")
#     print("Bye")
#     prnt("-------------")

# greet()
# greet()


# def greet():
#     print("Hello")
#     print("Hi")
#     print("Bye")
#     print("-------------")

# for _ in range(1,51):
#     greet()

# def greet():
#     print("Hello")
#     print("Hi")
#     print("Bye")
#     print("-------------")

# for i in range(1,51):
#     print(f"call {i}",greet())

# print("--------------------------")
# def addition(a,b):
#     print(f"addition of {a} and {b} is {a+b}")

# addition(10, 20)

# print("--------------------------")

# def addition(a, b, c):
#     print(f"addition of {a}, {b}, {c} is {a+b+c}")

# addition(10, 20, 30)

# print("------------------------------")

# def func():
                    #indentation eroor 
# func()

# print("---------------------------------")

# def func():      
#     pass      #kuch bhi nhi aayega output

# func()

# print("---------------------------------")

# function ke andar return or kuch bhi likha to output None aayega 

# def func():      #output : None
    
#     pass

# res = func()
# print(res)

# Function ke andar return likha to return value print honga
# ek return value print honga start wala other nhi hoga

# def func():      #output : hi
    
#     return "hi"
#     return "aa"

# res = func()
# print(res)


# def func():      #output : hi
    
#     return "hi"
#     return "hi"
#     return "Hello"

# res = func()
# print(res)


# def func():      #output : 1
    
#     return "1"

# res = func()
# print(res)


# def func():      #output : 1
    
#     return "1"
#     return 1

# res = func()
# print(res)


# def func():      #output : None
    
#     return 

# res = func()
# print(res)


# maine directly return mai None pass kiya to output None aayega

# def func():      #output : None
    
#     return None

# res = func()
# print(res)

# def func():
#     print("before return")  # output before return, hi
#     return "hi"             
#     print("after return")

# res = func()
# print(res)


# print("before defining func")

# def func():
#     print("inside function")  
#     return "hi"             
#     print("after return")

# print("before calling func")
# res = func()
# print("after calling func")
# print(res)


# In return multiple values we can pass 

# def func():
#     return 10, 20, 30, "hi", [1, 2, 3]    # Output : (10, 20, 30, 'hi', [1, 2, 3])

# res = func()
# print(res, type(res))


# def func():
#     return (10, 20, 30, "hi", [1, 2, 3])    # Output : (10, 20, 30, 'hi', [1, 2, 3])

# res = func()
# print(res)


# def operations(a,b):
#     return a+b, a-b, a*b, a//b 

# res = operations(20,10)
# print(res)


# arguments
#    formal
#    actual
#         positional
#         default
#         variable length
#         keyword
#         variable length keyword


# Positional

# def func(a, b, c, d): # Error TypeError: func() missing 4 required positional arguments: 'a', 'b', 'c', and 'd'
#     print(a, b, c, d)

# func()


# def func(a, b, c, d):                # Output : 1, 2, 3, 4
#     print(a, b, c, d)

# func(1, 2, 3, 4)


# def func(a, b, c, d, e):             # Output TypeError: func() missing 1 required positional argument: 'e'
#     print(a, b, c, d)

# func(1, 2, 3, 4)


# def func(a, b, c):          # TypeError: func() missing 3 required positional arguments: 'a', 'b', and 'c'
#     print(a, b, c)

# func()

# def func(a, b, c):  # TypeError: func() missing 1 required positional argument: 'c'
#     print(a, b, c)

# func(10, 20)

# default

# def func(a, b, c=30):    # default c value is 30
#     print(a, b, c)

# func(10, 20)


# def func(a, b, c = 30):    # default c value is 40 here because we alreaady pass argument for 'c'
#     print(a, b, c)

# func(10, 20, 40)


# def func(a, b, c = 30):    # TypeError: func() missing 1 required positional argument: 'b'
#     print(a, b, c)

# func(10)


# def func(a, b = 20, c = 30): 
#     print(a, b, c)

# func(10)


# def func(a, b = 20, c = 30):  # TypeError: func() missing 1 required positional argument: 'a'
#     print(a, b, c)

# func()


# def func(a = 10, b = 20, c = 30):  

# func()


# Variable length

# def func(*args):    # Output: () <class 'tuple'>
#     print(args,type(args))

# func()


# def func(*args):   
#     print(args,type(args))

# func(10, 20, 30, 40, 50, 60, 70, [4, 5, 6]) # min: 0 values and max : 

# def add_numbers(*args):
#     print(f"Sum: {sum(args)}")

# add_numbers(2, 3, 5) # Sum: 10
# add_numbers(1, 4, 7, 10) # Sum: 22


# def func(a, b, c = 20, *args):   # () <class 'tuple'>
#     print(args,type(args))


# func(10, 20)

# def func(a, b, c = 30, *args):   # 10 20 30 ()     this example is positional, default and variable length
#     print(a, b, c, args)

# func(10, 20)

# def func(a, b, c = 30, *args):   # 10 20 40 ()
#     print(a, b, c, args)

# func(10, 20, 40)

# def func(a, b, c = 30, *args):   # TypeError: func() missing 1 required positional argument: 'b'
#     print(a, b, c, args)

# func(10)


# def func(a, b, c = 30, *args):   # 10 20 50 ('s', 'l', 'm', [1, 3, 5])
#     print(a, b, c, args)

# func(10, 20, 50, "s", "l", "m", [1, 3, 5])

# keyword

# def func(a, b, c):
#     print(a, b, c)

# func(10, 20, 30)


# def func(a, b, c):
#     print(a, b, c)

# func(b = 10, a = 20, c = 30)


# Keyword length variable argument

# def func(a, b, c):
#     print(a, b, c)

# func(b = 10, a = 20, c = 30)


# def func(a, b, c):
#     print(a, b, c)

# func(b = 10, a = 20, c = 30)

# def func(**kwargs):   # output = {}
#     print(kwargs)

# func()

# def func(**kwargs):   # {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
#     print(kwargs) 

# func(a=10, b=20, c=30, d=40, e=50)


# def func(**kwargs):   # {'a': 10}
#     print(kwargs) 

# func(a=10)


# def func(**kwargs):   # TypeError: func() takes 0 positional arguments but 1 was given
#     print(kwargs) 

# func(10)


# def func(a, **kwargs):  # TypeError: func() takes 1 positional argument but 2 were given
#     print(kwargs) 

# func(10, 20)


def func(a, **kwargs): 
    print(kwargs) 

func(10, b=20)

# # def greet():
# #     print("Hello, welcome to function in python!")

# # greet()
# # greet()

# print("---------------------------------------------")

# # 1️⃣ Basic Function (No parameters)

# # def greet():

# #     print("Hello, welcome to function in python!")

# # greet()

# # 2️⃣ Function with Parameters (Input)

# # def greet_user(name):
# #     print(f"Hello, {name}!")

# # greet_user("Abhi")

# # def add(a, b):
# #     print(a + b)

# # add(10,20)

# # def greet(name):
# #     print(f"Hello, {name}!")

# # greet("Alice")  # Output: Hello, Alice!

# # def add(a, b):
# #     return a + b

# # result = add(5, 3)
# # print(result)  # Output: 8

# def func():
#     return 

# res = func()
# print(res)


# def func():
#     return 

# res = func()
# print(res)



# def add(a,b):
#     return a + b

# print(add(2,3))

# Palindrome String

# def is_palindrome(s):
#     return s == s[::-1]

# print(is_palindrome ("radar"))

print("-------------------------------")

#  Even or Odd

# def even_or_odd(n):
#     return "Even" if n % 2 == 0 else "Odd"

# print(even_or_odd(4))

print("-------------------------------")

# Reverse String

# def reverse_string(s):
#     return s[::-1]

# print(reverse_string("Hello"))

print("-------------------------------")

# Largest in List

# def max_in_list(lst):
#     return max(lst)

# print(max_in_list([4,1,5,7,9,8]))

print("-------------------------------")

# Square of a Number

# def square(n):
#     return n * n

# print(square(5))


print("-------------------------------")

# import math
# def area_circle(r):
#     return round(math.pi * r * r, 2)

# print(area_circle(5)) 

# Length of String

# def string_length(s):
#     return len(s)

# print(string_length("DipakMani"))


# print("------------------------")

# def sort_list(lst):
#     return sorted(lst)

# print(sort_list([5, 1, 4, 6]))

print("------------------------")

# Count Words in Sentence

# def count_words(s):
#     return len(s.split())

# print(count_words("This is Python"))  

# Convert to Upper Case

# def to_upper(s):
#     return s.upper()

# print(to_upper("hello"))  # Output: HELLO


# 20 Examples of Default and Positional Arguments
#  Default Greeting

# def greet(name="Guest"):
#     print(f"Hello, {name}!")

# greet()
# greet("Rohan")

#  Sum Function with Default

# def add(a, b=10):
#     return a + b

# print(add(4))
# print(add(3, 4))


# def power(base=2, exponent=3):
#     return base ** exponent

# print(power())           # Output: 8
# print(power(3))          # Output: 27
# print(power(3, 2))       # Output: 9


# def show_info(name, age = 18):
#     print(f"{name} is {age} years old.")

# show_info("Tom")               # Output: Tom is 18 years old.
# show_info("Jerry", age=5)      # Output: Jerry is 5 years old.

# def greet(first="John", last="Doe"):
#     print(f"Hello {first} {last}")

# greet()                         # Output: Hello John Doe
# greet(last="Smith")             # Output: Hello John Smith


# What is Function?

# Function is an organized block of reusable code
# Functions can be called n number of times
# Function contains set of instructions which perform specific tasks. Ex-Addition, Substraction

# withdraw
# take a loan
# credit
# link_with_aadhar

# There are two types of functions:-
# 1. Built-in 2. User-defined

# str1 = "dipak"
# print(len(str1))

# def function_name([parameters]):
#     statements1
#     statements2
#     statements3

# function_name()

# def display(message):
#     print("Welcome!")
#     print(message)

# display("Hello World")
# print('*' * 50)
# display("my world")


# def display():
#     print("Welcome")
#     message = input("Enter a message:")
#     print(message)

# display()
# print('-' * 50)
# display()


# parameters vs arguments

# parameters:- formal arguments
# arguments:- actual arguments

# def add(a,b):
#     print(a+b)

# add(10,20)
# add(100,200)
# add(200,400)


# Caculation of simple interest

# def simple_interest(p,n,r):
#     print("Principal amount is:",p)
#     print("number of years:",n)
#     print("rate of interest:",r)
#     si = (p*n*r)/100
#     print("Simple interest is:",si)

# simple_interest(10000,3,12.25)
# print("-" * 50)
# simple_interest(20000,7,10.15)